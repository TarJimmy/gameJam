<<<<<<< HEAD
import pygame,sys,math,random
=======
import pygame

class VueAccueil:
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
>>>>>>> ae3c301b7b7f589b342d3c401fff9aed58dc62a0
pygame.init()
#Titre de l'écran
pygame.display.set_caption("Accueil")
#Appliquer la taille de l'écran à l'attribut screen
screen = pygame.display.set_mode((800,400))
#background comprend l'image de fond
background = pygame.image.load('bg10.jpg')
running= True
#myFont=pygame.font.SysFont('Arial',30,bold=True)
#text=myFont.render('Bienvenue au jeu Walijeux',True,(255,255,255))
rectScreen = screen.get_rect()
police = pygame.font.Font("freesansbold.ttf",72)
texte = police.render("Walijeux",True,(255,0,0))
rectTexte = texte.get_rect()
rectTexte.center = rectScreen.center
while running :
    screen.blit(background,(0,-100))
    for event in pygame.event.get():
        if event.type== pygame.QUIT :
            running = False
    rectone= pygame.Rect(230,230,90,90)
    pygame.draw.rect(screen,(52,201,36),(rectone))
    screen.fill(pygame.Color("#FF0000"))
    screen.blit(texte,(80,80))
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
