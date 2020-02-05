import pygame
import math
from class_Player import Player
from class_Object import Object
from class_Npc import Npc
from class_Object import Object
class Game:
    def __init__(self, pos_initialP, pos_initialN, pos_initialO):
        cheminBackGround = 'images/backgrounds/'
        self.pos_initialP = pos_initialP
        self.pos_initialN = pos_initialN
        self.pos_initialO = pos_initialO
        cheminObject = 'images/objects/sol1.png'
        self.gravity = 2
        self.np = 0
        #Variable pour détecter si player proche de npc
        self.isNear = False
        #Valeurs X et Y du champ texte
        self.textX = 590
        self.textY = 300
        self.msg = "Hello, je suis ton père !"
        self.font = pygame.font.Font('freesansbold.ttf',32)
        #Pour vérifier qu'on peut toujours lancer le dialogue
        self.lancementDialogue = False
        #variable pour sauvegarder la position x du perso
        self.save = 0
        #Ordre des backgrounds
        self.bg = [
            pygame.image.load(cheminBackGround + 'bg1.jpg'),
            pygame.image.load(cheminBackGround + 'bg2.jpg'),
            pygame.image.load(cheminBackGround + 'bg3.jpg'),
            pygame.image.load(cheminBackGround + 'bg4.jpg'),
            pygame.image.load(cheminBackGround + 'bg5.jpg'),
            pygame.image.load(cheminBackGround + 'bg6.jpg'),
            pygame.image.load(cheminBackGround + 'bg7.jpg'),
            pygame.image.load(cheminBackGround + 'bg8.jpg'),
            pygame.image.load(cheminBackGround + 'bg9.jpg'),
            pygame.image.load(cheminBackGround + 'bg10.jpg')
        ]
        #generer notre joueur
        self.player = Player(
            self.pos_initialP[0],
            self.pos_initialP[1],
            self.pos_initialP[2],
            self.pos_initialP[3]
            )
        self.mesSols = []
        #generer notre npc
        self.npc = Npc(
            self.pos_initialN[0],
            self.pos_initialN[1],
            self.pos_initialN[2],
            self.pos_initialN[3]
        )
        #generer un objet
        self.object = Object(
            self.pos_initialO[0],
            self.pos_initialO[1],
            cheminObject
        )

    def addSol(self, x,y,cheminImage):
        sol = Object(x,y,cheminImage)
        self.mesSols.append(sol)

    def isCollisionNpc(self):
        distance = math.sqrt((math.pow(self.npc.x- self.player.x,2)) + (math.pow(self.npc.y - self.player.y,2)))
        if distance < self.player.width:
            return True
        #100 > le player n'a pas le droit de sauter
        elif distance < 100:
            self.isNear = True
            print("yoto")
        else:
            self.isNear = False

    def show_dialog(self,x,y,screen):
        texte = self.font.render(self.msg,True, (255,255,255))
        screen.blit(texte, (x,y))

    def blocage_affichage(self,screen):
        if self.isCollisionNpc():
            self.player.x = self.npc.x - self.player.width
            self.save = self.player.x
            self.lancementDialogue = True
        if self.lancementDialogue and self.save == self.player.x :
            self.show_dialog(self.textX,self.textY,screen)

    # def isCollisionObject(self):
    #     distance = math.sqrt((math.pow(self.object.rect.x- self.player.x,2)) + (math.pow(self.object.rect.y - self.player.y,2)))
    #     if distance < self.player.width:
    #         return True
    #         print("alow")
    #
    # def collision_object(self):
    #     if (self.player.x == self.object.rect.x) and (self.player.y + self.player.height) < self.object.rect.y:
    #         self.player.y = self.object.rect.y - self.player.height
    #         print("wola")

    def verifGravite(self):
        plateau11x = -30
        plateau12x = 960

        #Verifier que le joueur est dans le cadran
        if (plateau11x <= self.player.x and plateau12x >= self.player.x):
            i = 0
            #Verifier que le joueur est sur un sol
            while i < len(self.mesSols):
                solCourant = self.mesSols[i]
                if solCourant.rect.y - self.player.height - self.player.velocity <= self.player.y:
                    return True
                i += 1
            return False

    def gravite(self):
        if(self.verifGravite()==False):
            self.player.y += 7
            self.player.isJump = False
        if(self.player.y>390):
            self.player.y = 390

    def plateaux(self,screen):
        screen.blit(self.bg[self.np], (0, 0))

    def changerPlateaux(self):
        if self.player.x > 940:
            self.np += 1
            self.player.x = -15
            self.player.y = 390
        if self.player.x < -20 and self.np > 0:
            self.np -= 1
            self.player.x = 930
            self.player.y = 390
        if self.player.x < -20 and self.np == 0:
            self.player.x = 15
            self.player.y = 390

    def createSol(self):
        i = 0
        while i < 950:
            self.addSol(i-3,450,'images/objects/sol1.png')
            self.addSol(i-3,510,'images/objects/sol2.png')
            i += 62

    def afficherSol(self, screen):
        for solCourant in self.mesSols:
            screen.blit(solCourant.image,(solCourant.rect.x,solCourant.rect.y))

    def actualiser(self, screen):
        self.plateaux(screen)
        self.changerPlateaux()
        self.afficherSol(screen)
        self.player.draw(screen)
        self.npc.draw(screen)
        self.object.draw(screen)
        self.blocage_affichage(screen)
        # self.collision_object()
