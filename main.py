import pygame
from class_Game import Game
from parametre import Parametre
from class_Player import Player
from class_Accueil import Accueil
from class_Histoire import Histoire
pygame.init()
#order : x,y, width, height
pos_initialP = [40, 40, 40, 60]
pos_initialN = [700, 395, 40, 60]
pos_initialO = [100, 420]
#creer l'unique objet jeu, le joueur et le npc font partie du jeu
game = Game(pos_initialP,pos_initialN,pos_initialO)
game.initMap()
#Variable en fonction que ce que l'on doit afficher

#cree l'unique objet parametre
param = Parametre()
clock = pygame.time.Clock()
acceuil = Accueil()
continu = acceuil.afficher()
if continu:
    running = True
    pygame.display.set_caption("Earth Zero²")
    son= pygame.mixer.Sound("jumping.wav")
    sonfond=pygame.mixer.Sound("fond.wav")
    screen = pygame.display.set_mode((game.width,game.height))
    MomentHistoire = True

    #boucle tant que cette condition est vrai
    while running:
        if MomentHistoire == True:
            game.afficherHistoire(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
                    if event.button == 1: # 1= clique gauche
                        if game.histoire.buttonNext.isClicked(event.pos):
                            MomentHistoire = False
                            game.numHistoire +=1
                            game.npModif = False
        else:
            #Affiche le jeu
            clock.tick(40)
            sonfond.play(loops=-1, maxtime=0 , fade_ms=0)
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # if keys[pygame.K_LEFT]:
            #     game.player.move_left()
            #
            # elif keys[pygame.K_RIGHT]:
            #     game.player.move_right()
            # else:
            #     game.player.no_move()
            #
            # if not (game.player.isJump):
            #     #Si la touche espace est enfoncée et si le player n'est pas proche du npc
            #     if keys[pygame.K_SPACE] and not (game.isNear):
            #         game.player.jump()
            #         son.play()
            #     else:
            #         game.gravite()
            # else:
            #     game.player.doJump()

            # game.player.do()


            game.actualiser(screen)
            if game.np==3 and game.npModif==True or game.np==10:
                MomentHistoire = True
        pygame.display.flip()
pygame.quit()
