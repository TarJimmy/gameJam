import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('images/objects/sol1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
