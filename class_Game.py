import pygame
import math, random, sys
from class_Player import Player
from class_Object import Object
from class_Npc import Npc
from class_Histoire import Histoire
class Game:
    def __init__(self, pos_initialP, pos_initialN, pos_initialO):
        cheminBackGround = 'images/backgrounds/'
        cheminObject = 'images/objects/sol1.png'
        self.maps = []
        self.formatsMaps = []
        self.mapCourant = None
        #Mesure du temps
        self.frame_count = 0
        self.frame_rate = 60
        #Temps original
        self.start_time = 90
        #Position initial du perso
        self.pos_initialP = pos_initialP
        self.pos_initialN = pos_initialN
        self.pos_initialO = pos_initialO
        #Force de la gravité
        self.gravity = 2
        #Numéro du background
        self.np = 0
        #Largeur de l'écran
        self.width = 960
        #Hauteur de l'écran
        self.height = 568
        #Classe pour raconter l'histoire du jeu
        self.histoire = Histoire()
        #Numéro de l'histoire courante
        self.numHistoire = 1
        #Le numero de page à été modifié (sert pour laffichage de l'histoire)
        self.npModif = False
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

    def afficherHistoire(self, screen):
        self.histoire.afficher(screen,self.numHistoire)

    def addSol(self, x,y,cheminImage):
        sol = Object(x,y,cheminImage)
        self.mesSols.append(sol)

    def addFormatMap(self,map):
        self.formatsMaps.append(map)
    #Crée toutes les formations de maps
    def createFormatMap(self):
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        print(self.formatsMaps)
    #Initialise toutes les maps (en créant les blocs associé)
    def initMap(self):
        self.createFormatMap()
        y = -35
        i = 0
        tab2 = []
        for tab in self.formatsMaps:
            tab2.clear()
            for ligne in tab:
                x = -30
                y+= 60
                for solCourant in ligne:
                    x += 62
                    if solCourant == 1:
                        sol = Object(x,y,"images/objects/plateau1.png")
                        tab2.append(sol)
            self.maps.append(tab2)
        print(self.maps)
    #Affiche la map séléctionné
    def afficherMap(self, screen):
        recupMap = self.maps[0]
        for solCourant in recupMap:
            screen.blit(solCourant.image,(solCourant.rect.x,solCourant.rect.y))

    def isCollisionNpc(self):
        distance = math.sqrt((math.pow(self.npc.x- self.player.x,2)) + (math.pow(self.npc.y - self.player.y,2)))
        if distance < self.player.width:
            return True
        #100 > le player n'a pas le droit de sauter
        elif distance < 100:
            self.isNear = True
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
            # for solCourant in self.
            #     solCourant = self.mesSols[i]
            #     if solCourant.rect.y - self.player.height - self.player.velocity <= self.player.y:
            #         return True
            #     i += 1
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
            self.npModif = True
        if self.player.x < -20 and self.np > 0:
            self.np -= 1
            self.player.x = 930
            self.player.y = 390
        if self.player.x < -20 and self.np == 0:
            self.player.x = 15
            self.player.y = 390

    def actualiser(self, screen):
        W, H = 1000, 500
        HW, HH = W / 2, H / 2
        AREA = W * H
        BLACK = (0, 0, 0, 255)
        WHITE = (0, 255, 0, 255)
        self.plateaux(screen)
        self.changerPlateaux()
        self.afficherMap(screen)
        self.player.do()
        self.player.draw(screen)
        PLATFORMS = self.player.platforms()
        PLATFORMS.add(self.player.platform(0, H - 10, W))
        PLATFORMS.add(self.player.platform(200, 400, 100))
        PLATFORMS.add(self.player.platform(300, 300, 100))
        # for i in range(0, 50):
        # 	PLATFORMS.add(self.player.platform(random.randint(0, W - 50), random.randint(50, H - 60), 50))
        PLATFORMS.do(self.player)
        # self.npc.draw(screen)
        # self.object.draw(screen)
        # self.blocage_affichage(screen)
        # self.collision_object()
