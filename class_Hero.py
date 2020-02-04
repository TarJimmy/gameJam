import pygame
from class_Inventaire import inventaire

class Hero(self):
    def __init__(self, nom):
        #Le nom du joueur
        self.nom = nom
        #Oxygene maximum du joueur
        self.OxygeneMax = 100
        #Oxygene courant du joueur
        self.Oxgene = self.OxygeneMax
        #Vie du joueur
        self.vie = 50
        #Vistesse du joueur
        self.velocity = 5
        #inventaire
        self.inventaire = Inventaire()
    def move_left(self):
        #délacement gauche
        code = 1 #a supprimer

    def move_right(self):
        #deplacement droite
        code = 1 #a supprimer

    def move_down(self):
        #déplacement bas
        code = 1 #a supprimer

    def move_up(self):
        #deplacement haut
        code = 1 #a supprimer
