import pygame
from view.VueAccueil import VueAccueil


class Controler:

    def __init__(self):
        pygame.init()
        self.accueil = VueAccueil()
        self.game = None
        accueil.afficher()
