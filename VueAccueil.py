import pygame,sys,math,random
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
