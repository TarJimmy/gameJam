import pygame
from class_Button import Button
from class_Credit import Credit
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
        self.boutonCredit = Button(500,250,"images/boutons/boutonCredit.gif")
        self.boutonCredit.redimensionne(180,47)
        self.logo = Button(275,10,"images/boutons/logo.png")
        self.logo.redimensionne(230,200)
        self.credit = Credit()

    #fonction qui affiche l'acceuil
    def afficher(self):

        #Met l'attribut d'affichage à True
        self.running = True
        #Tant qu'on continue à afficher la fenetre
        credit = False
        continu = True
        
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

            else:
                self.screen = pygame.display.set_mode((self.width,self.height))
                #Charge le background
                self.screen.blit(self.background, (0,0))
                #Met à jour l'écran
                self.screen.blit(self.boutonJouer.image, (self.boutonJouer.rect.x,self.boutonJouer.rect.y))
                self.screen.blit(self.boutonCredit.image, (self.boutonCredit.rect.x,self.boutonCredit.rect.y))
                self.screen.blit(self.logo.image, (self.logo.rect.x,self.logo.rect.y))

                #Parcours tous les évenements possibles
                for event in pygame.event.get():
                    # si l'evenement est fermeture de fenetre
                    if event.type == pygame.QUIT:
                        self.running = False
                        continu = False
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            if self.boutonJouer.isClicked(event.pos):
                                self.running = False
                            if self.boutonCredit.isClicked(event.pos):
                                credit = True
            pygame.display.flip()
        return continu
