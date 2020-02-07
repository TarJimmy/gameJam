import pygame
from class_Game import Game
from parametre import Parametre
from class_Player import Player
from class_Accueil import Accueil
from class_Histoire import Histoire
pygame.init()
pygame.font.init()
#order : x,y, width, height
pos_initialP = [40, 40, 64, 60]
pos_initialN = [700, 395, 40, 60]
pos_initialO = [100, 420]
#creer l'unique objet jeu, le joueur et le npc font partie du jeu
param = Parametre()
continu = True
while continu:
    #creer l'unique objet jeu, le joueur et le npc font partie du jeu
    game = Game(pos_initialP,pos_initialN,pos_initialO)
    game.initMap()
    #cree l'unique objet parametre
    clock = pygame.time.Clock()
    acceuil = Accueil()
    continu = acceuil.afficher()
    running = True
    pygame.display.set_caption("Earth Zero²")
    #fond sonore
    SIFFLEMENT = pygame.mixer.music.load("sons/fond.wav")
    pygame.mixer.music.play(20, 0.0)
    #effet sonore
    sonjump=pygame.mixer.Sound("sons/jumping.wav")

    screen = pygame.display.set_mode((game.width,game.height))
    #Variable en fonction que ce que l'on doit afficher
    MomentHistoire = True
    retourAccueil = False
    if continu:
        #boucle tant que cette condition est vrai
        while running and retourAccueil==False:
            if game.player.oxygene < 0:
                game.numHistoire = 4
                game.afficherHistoire(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        continu = False
                    elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
                        if event.button == 1: # 1= clique gauche
                            if game.histoire.buttonNext.isClicked(event.pos):
                                MomentHistoire = False
                                retourAccueil = True
                                running = False
            elif MomentHistoire == True:
                game.afficherHistoire(screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        continu = False
                    elif event.type == pygame.MOUSEBUTTONUP: # quand je relache le bouton
                        if event.button == 1: # 1= clique gauche
                            if game.histoire.buttonNext.isClicked(event.pos):
                                MomentHistoire = False
                                game.numHistoire +=1
                                game.npModif = False
                                if game.np==(game.nbBg-1):
                                    retourAccueil = True
            elif retourAccueil:
                if not MomentHistoire:
                    running = False
            else:
                #Affiche le jeu
                clock.tick(30)
                # sonfond.play(loops=-1, maxtime=0 , fade_ms=0)
                keys = pygame.key.get_pressed()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        continu = False
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
                if game.np==7 and game.npModif==True or game.np==(game.nbBg-1):
                    MomentHistoire = True
            if game.lancementDialogue:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            if event.pos[1] >= game.bY:
                                if game.buttons[(len(game.quest.reponsesFausses))].isClicked(event.pos):
                                # or self.bouton2.isClicked(event.pos) or self.bouton3.isClicked(event.pos)
                                # or self.bouton4.isClicked(event.pos) or self.bouton5.isClicked(event.pos):
                                    game.solution=True
                                    game.mesNpc[game.np].end = True
                                    game.player.oxygene += game.mesNpc[game.np].bonus
                                    game.numQuest += 1
                                    print("REPONSE VRAIE !")
                                else:
                                    game.solution=True
                                    game.mesNpc[game.np].end = True
                                    game.player.oxygene -= 150
                                    game.numQuest += 1
                                    print("REPONSE FAUSSE !")

            pygame.display.flip()
pygame.quit()
