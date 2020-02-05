import pygame
from class_Game import Game
from parametre import Parametre
from class_Player import Player
from class_Accueil import Accueil

pygame.init()
#order : x,y, width, height
pos_initialP = [40, 40, 40, 60]
pos_initialN = [700, 395, 40, 60]
pos_initialO = [100, 420]
#creer l'unique objet jeu, le joueur et le npc font partie du jeu
game = Game(pos_initialP,pos_initialN,pos_initialO)
#Variable en fonction que ce que l'on doit afficher

#cree l'unique objet parametre
param = Parametre()
clock = pygame.time.Clock()
acceuil = Accueil()
continu = acceuil.afficher()
print(continu)
if continu:
    running = True
    game.createSol()
    pygame.display.set_caption("Earth Zero²")
    son= pygame.mixer.Sound("jumping.wav")
    sonfond=pygame.mixer.Sound("fond.wav")

<<<<<<< HEAD
    screen = pygame.display.set_mode((game.width,game.height))
    #boucle tant que cette condition est vrai
    while running:
    #Affiche le jeu
        clock.tick(80)
        sonfond.play(loops=-1, maxtime=0 , fade_ms=0)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
=======
screen = pygame.display.set_mode((param.verifWidth(960),param.verifHeight(568)))

running = True
game.createSol()
pygame.display.set_caption("Earth Zero²")
son= pygame.mixer.Sound("jumping.wav")
# sonfond=pygame.mixer.Sound("fond.wav")
#boucle tant que cette condition est vrai
while running:
    clock.tick(80)
    # sonfond.play(loops=-1, maxtime=0 , fade_ms=0)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
            if event.button == 1: # 1= clique gauche
                for buttonCourant in game.mesSols:
                    if buttonCourant.isClicked(event.pos):
                        print("Je clique sur mon sol")
>>>>>>> 261ed00566dd3273dbc3621340191d645193a542

        if keys[pygame.K_LEFT]:
            game.player.move_left()

        elif keys[pygame.K_RIGHT]:
            game.player.move_right()
        else:
            game.player.no_move()

        if not (game.player.isJump):
            #Si la touche espace est enfoncée et si le player n'est pas proche du npc
            if keys[pygame.K_SPACE] and not (game.isNear):
                game.player.jump()
                son.play()
            else:
                game.gravite()
        else:
            game.player.doJump()

        game.actualiser(screen)
        pygame.display.flip()
pygame.quit()
