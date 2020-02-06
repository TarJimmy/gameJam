import pygame

class Npc(pygame.sprite.Sprite):
    """docstring for npc."""

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.end = False
        cheminImage = "images/npc/"
        self.char = pygame.image.load(cheminImage+'L9E.png')

    def draw(self,window):
        #On retire le npc s'il a donné la solution
        if self.end:
            self.x = 1000
            self.y = 1000
        else:
            window.blit(self.char,(self.x,self.y))
