import pygame
from class_Game import Game
from parametre import Parametre
from class_Player import Player

pygame.init()
#order : x,y, width, height
pos_initialP = [40, 40, 40, 60]
pos_initialN = [700, 395, 40, 60]
#creer l'unique objet jeu, le joueur et le npc font partie du jeu
game = Game(pos_initialP,pos_initialN)
#cree l'unique objet parametre
param = Parametre()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((param.verifWidth(960),param.verifHeight(568)))

running = True
game.createSol()
#boucle tant que cette condition est vrai
while running:
    clock.tick(80)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_LEFT]:
        game.player.move_left()

    elif keys[pygame.K_RIGHT]:
        game.player.move_right()
    else:
        game.player.no_move()

    if not (game.player.isJump):
        if keys[pygame.K_SPACE]:
            game.player.jump()
        else:
            game.gravite()
    else:
        if game.player.jumpCount >= -7:
            # neg = 1
            # if game.player.jumpCount < 0:
            #     neg = -1
            game.player.y -= (game.player.jumpCount * abs(game.player.jumpCount)) * 0.5
            game.player.jumpCount -= 1
        else:
            game.player.isJump = False
            game.player.jumpCount = 7
    game.actualiser(screen)
    pygame.display.flip()
pygame.quit()
