import pygame
from class_Player import Player
from class_Object import Object
class Game:
    def __init__(self, pos_initital):
        cheminBackGround = 'images/backgrounds/'
        self.pos_initital = pos_initital
        self.gravity = 2
        self.np = 0
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
            self.pos_initital[0],
            self.pos_initital[1],
            self.pos_initital[2],
            self.pos_initital[3]
            )
        self.mesSols = []

    def addSol(self, x,y,cheminImage):
        sol = Object(x,y,cheminImage)
        self.mesSols.append(sol)

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
            print("jy passe)")
            self.player.y += 7
            self.player.isJump = False
        else:
            print("jy passe pas")
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
            self.addSol(i,450,'images/objects/sol1.png')
            self.addSol(i,510,'images/objects/sol2.png')
            i += 62

    def afficherSol(self, screen):
        for solCourant in self.mesSols:
            screen.blit(solCourant.image,(solCourant.rect.x,solCourant.rect.y))

    def actualiser(self, screen):
        self.plateaux(screen)
        self.changerPlateaux()
        self.afficherSol(screen)
        self.player.draw(screen)
