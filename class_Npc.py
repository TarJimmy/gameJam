import pygame, random
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
        self.bonus = random.randint(300, 500)
        print(self.bonus)

    def draw(self,window):
        #On retire le npc s'il a donné la solution
        if not self.end:
            window.blit(self.char,(self.x,self.y))
            self.bonus = 0
