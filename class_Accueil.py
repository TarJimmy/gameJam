import pygame
from class_Button import Button
from class_Credit import Credit
from class_RegleJeux import RegleJeux
from class_Classement import Classement
class Accueil:
    #Construteur de l'accueil


    def __init__(self):
        #Largeur de l'écran
        self.width = 800
        #Hauteur de l'écran
        self.height = 400
        #Titre de l'écran
        pygame.display.set_caption("Accueil")
        #Appliquer la taille de l'écran à l'attribut screen
        self.screen = pygame.display.set_mode((self.width,self.height))
        #background comprend l'image de fond
        self.background = pygame.image.load('images/backgrounds/bg10.jpg')
        #redimensionne l'image
        self.background = pygame.transform.scale(self.background,((self.width),self.height))
        #running est l'attribut ui précise si l'écran est activé
        self.running = False

        # RED = pygame.Color(255, 0, 0)
        # size = (50, 50)
        # rect_filled = pygame.Surface(size)
        # self.bouton = pygame.draw.rect(rect_filled, RED, rect_filled.get_rect())
        # self.bouton = pygame.image.load("images/joueur/L11E.png").convert_alpha()
        # # self.bouton_rect = pygame.Rect(200, 200, 64, 64) ## CONNAITRE LE RECTANGLE
        # self.bouton_rect = self.bouton.get_rect() ## CONNAITRE LE RECTANGLE
        # self.font = pygame.font.SysFont('helvetic', 70)
        # self.TEXT = 'Rien..'
        # self.rouge = (255,0,0)
        self.boutonJouer = Button(100,250,"images/boutons/boutonJouer.gif")
        self.boutonJouer.redimensionne(180,47)
        self.boutonQuitter = Button(500,250,"images/boutons/boutonQuitter.gif")
        self.boutonQuitter.redimensionne(228,47)
        self.boutonCredit = Button(self.width-134,self.height -35,"images/boutons/boutonCredit.gif")
        self.boutonCredit.redimensionne(129,30)
        self.boutonRegle = Button(220,310,"images/boutons/boutonRegleJeu.gif")
        self.boutonRegle.redimensionne(343,47)
        self.boutonRecord = Button(5,self.height -35,"images/boutons/boutonRecord.gif")
        self.boutonRecord.redimensionne(151,30)
        self.logo = Button(275,10,"images/boutons/logo.png")
        self.logo.redimensionne(230,200)
        self.credit = Credit()
        self.regle = RegleJeux()
        self.record = Classement()

    #fonction qui affiche l'acceuil
    def afficher(self):

        #Met l'attribut d'affichage à True
        self.running = True
        #Tant qu'on continue à afficher la fenetre
        credit = False
        continu = True
        regleJeu = False
        record = False
        while self.running:
            if credit:
                self.screen = pygame.display.set_mode((self.credit.width,self.credit.height))
                #Affiche le titre des roles
                self.credit.afficher(self.screen)
                for event in pygame.event.get():
                    # si l'evenement est fermeture de fenetre
                    if event.type == pygame.QUIT:
                        self.running = False
                        continu = False
                    elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
                        if event.button == 1: # 1= clique gauche
                            if self.credit.buttonBack.isClicked(event.pos):
                                credit = False
            elif regleJeu:
                self.screen = pygame.display.set_mode((self.regle.width,self.regle.height))
                #Affiche le titre des roles
                self.regle.afficher(self.screen)
                for event in pygame.event.get():
                    # si l'evenement est fermeture de fenetre
                    if event.type == pygame.QUIT:
                        self.running = False
                        continu = False
                    elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
                        if event.button == 1: # 1= clique gauche
                            if self.regle.buttonBack.isClicked(event.pos):
                                regleJeu = False
            elif record:
                self.screen = pygame.display.set_mode((self.record.width,self.record.height))
                #Affiche le titre des roles
                self.record.afficher(self.screen)
                for event in pygame.event.get():
                    # si l'evenement est fermeture de fenetre
                    if event.type == pygame.QUIT:
                        self.running = False
                        continu = False
                    elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
                        if event.button == 1: # 1= clique gauche
                            if self.record.buttonBack.isClicked(event.pos):
                                record = False

            else:
                self.screen = pygame.display.set_mode((self.width,self.height))
                #Charge le background
                self.screen.blit(self.background, (0,0))
                #Met à jour l'écran
                self.screen.blit(self.boutonRegle.image,(self.boutonRegle.rect.x,self.boutonRegle.rect.y))
                self.screen.blit(self.boutonJouer.image, (self.boutonJouer.rect.x,self.boutonJouer.rect.y))
                self.screen.blit(self.boutonQuitter.image, (self.boutonQuitter.rect.x,self.boutonQuitter.rect.y))
                self.screen.blit(self.boutonCredit.image, (self.boutonCredit.rect.x,self.boutonCredit.rect.y))
                self.screen.blit(self.boutonRecord.image, (self.boutonRecord.rect.x,self.boutonRecord.rect.y))
                self.screen.blit(self.logo.image, (self.logo.rect.x,self.logo.rect.y))

                #Parcours tous les évenements possibles
                for event in pygame.event.get():
                    # si l'evenement est fermeture de fenetre
                    if event.type == pygame.QUIT :
                        self.running = False
                        continu = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            if self.boutonJouer.isClicked(event.pos):
                                self.running = False
                            if self.boutonCredit.isClicked(event.pos):
                                credit = True
                            if self.boutonRegle.isClicked(event.pos):
                                regleJeu = True
                            if self.boutonRecord.isClicked(event.pos):
                                record = True
                            if  self.boutonQuitter.isClicked(event.pos):
                                self.running = False
                                continu = False
            pygame.display.flip()
        return continu
