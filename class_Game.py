import pygame
import math, random, sys
from class_Player import Player
from class_Object import Object
from class_Npc import Npc
from class_Histoire import Histoire
from class_Oxygene import Oxygene
from class_Question import Question
from class_Button import Button

class Game:
    def __init__(self, pos_initialP, pos_initialN, pos_initialO):
        cheminBackGround = 'images/backgrounds/'
        cheminObject = 'images/objects/sol1.png'
        self.maps = []
        self.formatsMaps = []
        #Mesure du temps
        self.frame_count = 0
        self.frame_rate = 60
        #Temps original
        self.start_time = 90
        self.mapCourante= None
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
        #Valeurs X et Y du champ question
        self.quX = 20
        self.quY = 475
        #Valeurs X et Y des reponses
        self.rX = 40
        self.rY = 515
        # Valeurs X et Y des boutons
        self.bX = 20
        self.bY = 505
        self.solution = False
        #Compteur de question
        self.numQuest = 1
        self.msg = None
        self.font = pygame.font.Font('freesansbold.ttf',15)
        #Pour vérifier qu'on peut toujours lancer le dialogue
        self.lancementDialogue = False
        #variable pour sauvegarder la position x du perso
        self.save = 0
        self.buttons = []
        self.quest = Question()
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
        self.nbBg = len(self.bg)
        #generer notre joueur
        self.player = Player(
            self.pos_initialP[0],
            self.pos_initialP[1],
            self.pos_initialP[2],
            self.pos_initialP[3]
            )
        self.mesSols = []
        #generer notre npc
        self.mesNpc = []
        #generer un objet
        # self.object = Object(
        #     self.pos_initialO[0],
        #     self.pos_initialO[1],
        #     cheminObject
        # )

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
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 3, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 1, 0, 0, 1, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1, 0, 1],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.addFormatMap(map)
        map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]]
        self.addFormatMap(map)

    #Initialise toutes les maps (en créant les blocs associé)
    def initMap(self):
        self.createFormatMap()
        i = 0
        for mapCourante in self.formatsMaps:
            y = -35
            tab = []
            for ligne in mapCourante:
                x = -30
                y+= 60
                for numCourant in ligne:
                    x += 62
                    if numCourant == 1:
                        sol = Object(x,y,"images/objects/plateau1.png")
                        tab.append(sol)
                    if numCourant == 2:
                        sol = Object(x,y,"images/objects/plateau1.png")
                        oxygene = Oxygene(x ,y - 41)
                        tab.append(sol)
                        tab.append(oxygene)
                    if numCourant ==3:
                        sol = Object(x+20,y,"images/objects/plateau1.png")
                        self.mesNpc.append(Npc(x,y-40))
                        tab.append(sol)
            self.maps.append(tab)
        self.mapCourante = self.maps[0]
    #Affiche la map séléctionné
    def afficherMap(self, screen):

        for solCourant in self.mapCourante:
            screen.blit(solCourant.image,(solCourant.rect.x,solCourant.rect.y))

    def isCollisionNpc(self):
        distance = math.sqrt((math.pow(self.mesNpc[self.np].x- self.player.x,2)) + (math.pow(self.mesNpc[self.np].y - self.player.y,2)))
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

    # def blocage_affichage(self,screen):
    #     if self.isCollisionNpc():
    #         self.player.x = self.npc.x - self.player.width
    #         self.save = self.player.x
    #         self.lancementDialogue = True
    #     if self.lancementDialogue and self.save == self.player.x :
    #         self.show_dialog(self.textX,self.textY,screen)

    def blocage(self):
        if self.isCollisionNpc():
            self.player.x = self.mesNpc[self.np].x - self.player.width
            self.save = self.player.x
            self.lancementDialogue = True

    def isCollisionObject(self):
        distance = math.sqrt((math.pow(self.object.x - self.player.x,2)) + (math.pow(self.object.y - self.player.y,2)))
        if distance < self.player.width:
            return True
        else:
            return False

    def collision_object(self,objet):
        if (self.player.x == self.object.rect.x) and (self.player.y + self.player.height) < self.object.rect.y:
            self.player.y = self.object.rect.y - self.player.height

    def initBoutonQuestion(self):
        self.buttons.clear()
        i = 0
        taille = len(self.quest.reponsesFausses)
        distance = 0
        while i < taille:
            self.buttons.append(Button(distance+self.bX,self.bY,"images/boutons/boutonReponse.png"))
            i += 1
            distance = i*(930//(taille+1))
        self.buttons.append(Button(distance+self.bX,self.bY,"images/boutons/boutonReponse.png"))

    def afficherQuestion(self,screen):
        if self.lancementDialogue and self.save == self.player.x :
            pygame.draw.rect(screen,(255,25,255),(18,470,930,90))
            self.quest.recupQuestionNum(self.numQuest)
            self.msg = self.quest.question
            self.show_dialog(self.quX,self.quY,screen)
            self.initBoutonQuestion()
            i=0
            distance = 0
            taille = len(self.quest.reponsesFausses)
            while i < taille:
                self.msg = self.quest.reponsesFausses[i]
                self.buttons[i].redimensionne(930//(taille+1),50)
                self.buttons[i].draw(screen)
                self.show_dialog(distance+self.rX,self.rY,screen)
                i += 1
                distance = i*(930//(taille+1))
            self.msg = self.quest.reponseJuste
            self.buttons[taille].redimensionne(930//(taille+1),50)
            self.buttons[taille].draw(screen)
            self.show_dialog(distance+self.rX,self.rY,screen)

    def afficherSolution(self,screen):
        pygame.draw.rect(screen,(255,25,255),(18,470,930,90))
        self.msg = self.quest.solution
        self.show_dialog(self.rX,self.rY,screen)

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
            # self.player.y = 390
            self.npModif = True
            self.mapCourante.clear()
            self.mapCourante = self.maps[self.np]
            #Pour arreter d'afficher la solution quand on change de map
            self.solution = False
        if self.player.x < -20 and self.np > 0:

            self.player.x = self.pos_initialP[0]
            self.player.y = self.pos_initialP[1]

        if self.player.x < -20 and self.np == 0:
            self.player.x = 15
            # self.player.y = 390
        if self.player.y > 568:
            self.player.x = self.pos_initialP[0]
            self.player.y = self.pos_initialP[1]

    def testCollision(self):
        if not self.player.falling: return False
        for solCourant in self.mapCourante:
            # print(solCourant)
            result = solCourant.test(self.player)
            # print(result)
            if result:
                self.player.currentPlatform = result
                self.player.y = result.y
                self.player.falling = False
                return True
        return False
    def do(self):
        self.testCollision(self.player)
        self.afficherMap()

    def actualiser(self, screen):
        self.plateaux(screen)
        self.changerPlateaux()
        self.afficherMap(screen)
        self.testCollision()
        self.player.do(self)
        self.player.draw(screen)
        self.mesNpc[self.np].draw(screen)
        # self.object.draw(screen)
        self.isCollisionNpc()
        self.blocage()
        if not self.solution:
            self.afficherQuestion(screen)
        else:
            self.afficherSolution(screen)
        # PLATFORMS = self.player.platforms()
        # PLATFORMS.add(self.player.platform(0, H - 10, W))
        # PLATFORMS.add(self.player.platform(200, 400, 100))
        # PLATFORMS.add(self.player.platform(300, 300, 100))
        # for i in range(0, 50):
        # 	PLATFORMS.add(self.player.platform(random.randint(0, W - 50), random.randint(50, H - 60), 50))
        # self.do()
        # self.npc.draw(screen)
        # self.object.draw(screen)
        # self.blocage_affichage(screen)
        # self.collision_object()
