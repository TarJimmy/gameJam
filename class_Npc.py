import pygame

class Npc(pygame.sprite.Sprite):
    """docstring for npc."""

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lose = False
        cheminImage = "images/npc/"
        self.let_pass = [
            #image suppr, a recup pygame.image.load(cheminImage+'L10E.png'),
            pygame.image.load(cheminImage+'L11E.png'),
            pygame.image.load(cheminImage+'L7E.png')
        ]
        self.count = 0
        self.char = pygame.image.load(cheminImage+'L9E.png')

    def draw(self,window):
        if self.lose:
            window.blit(self.let_pass[self.count], (self.x,self.y))
            self.count += 1
        else:
            window.blit(self.char,(self.x,self.y))
