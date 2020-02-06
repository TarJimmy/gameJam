import random
import pygame
from class_Object import Object

class Oxygene(Object):
    def __init__(self,x,y,cheminImage = "images/objects/oxygene.png", type = "oxygene"):
        super().__init__(x,y,cheminImage, type)
        self.bonus = random.randint(100, 300)

    def test(self, player):
        return self.rect.colliderect(pygame.Rect(player.x,player.y,player.width,player.height))
