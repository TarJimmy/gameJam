import pygame

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
        self.background = pygame.image.load('images/ciel.jpg')
        #redimensionne l'image
        self.background = pygame.transform.scale(self.background,((self.width),self.height))
        #running est l'attribut ui précise si l'écran est activé
        self.running = False

    #fonction qui affiche l'acceuil
    def afficher(self):
        #Met l'attribut d'affichage à True
        self.running = True
        #Tant qu'on continue à afficher la fenetre
        while self.running:
            #Charge le background
            self.screen.blit(self.background, (0,0))
            #Met à jour l'écran
            pygame.display.flip()

            #Parcours tous les évenements possibles
            for event in pygame.event.get():
                # si l'evenement est fermeture de fenetre
                if event.type == pygame.QUIT:
                    self.running = False
                    print("Fermeture de l'accueil")

#A supprimer, c'est pour tester directement l'accueil
pygame.init()

accueil = VueAccueil()
accueil.afficher()

acceuil = VueAccueil()
acceuil.afficher()
