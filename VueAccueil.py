import pygame
from class_Button import Button
from class_Credit import Credit

class VueAccueil:
    #Construteur de l'accueil


    def __init__(self):
#
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

        self.credit = Credit(self.screen)

    def initCredit():
        self.credit.addRoles("Saint-Laurent-Cyr Mark-Olivier", "Game Designer")
        self.credit.addRoles("Jimmy Tardy", "Developpeur")
        self.credit.addRoles("Cesar Watrin", "Developpeur")
        self.credit.addRoles("Amine Benmansour", "Developpeur")
        self.credit.addRoles("Lucas Zaetta", "Developpeur")

        self.credit.addSource("exemple", "unesource.com")
        self.credit.addSource("Exemple", "une deuxieme source.com")

    #
    # def gerer_event(self):
    #
    #     ## Si le focus est sur la fenêtre.
    #     if pygame.mouse.get_focused():
    #         ## Trouve position de la souris
    #         x, y = pygame.mouse.get_pos()
    #
    #         ## S'il y a collision:
    #         collide = self.bouton_rect.collidepoint(x, y)
    #
    #         if collide:
    #             print("Je suis dessus")
    #         else:
    #             print("Rien")

    #fonction qui affiche l'acceuil
    def afficher(self):

        #Met l'attribut d'affichage à True
        self.running = True
        #Tant qu'on continue à afficher la fenetre
        while self.running:
            #Charge le background
            self.screen.blit(self.background, (0,0))
            #Met à jour l'écran
            # self.screen.blit(self.bouton, (200,200))
            # self.screen.blit(self.bouton, self.bouton_rect)
            # pygame.draw.rect(self.screen, self.rouge, self.bouton_rect)
            self.screen.blit(self.boutonJouer.image, (self.boutonJouer.rect.x,self.boutonJouer.rect.y))
            self.screen.blit(self.boutonCredit.image, (self.boutonCredit.rect.x,self.boutonCredit.rect.y))
            self.screen.blit(self.logo.image, (self.logo.rect.x,self.logo.rect.y))
            # self.bouton.fill((255,20,0))
            # text = self.font.render(self.TEXT, 1, (255,255,255))
            # self.screen.blit(text, (50, 500))

            ## Gérer les événements.
            # accueil.gerer_event()

            pygame.display.flip()

            #Parcours tous les évenements possibles
            for event in pygame.event.get():
                # si l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    self.running = False
                    print("Fermeture de l'accueil")
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.boutonJouer.isClicked(event.pos):
                            print("Je clique sur boutonJouer")
                        if self.boutonCredit.isClicked(event.pos):
                            print("Je clique sur boutonCrédit")
                            self.credit.afficher()


#A supprimer, c'est pour tester directement l'accueil
pygame.init()
accueil = VueAccueil()
accueil.afficher()
