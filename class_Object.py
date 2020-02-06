import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,cheminImage):
        super().__init__()
        self.image = pygame.image.load(cheminImage)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x1 = x
        self.x2 =  x + 67
        self.y = y - 41
        # self.x1 = int(x)
        # self.y = int(y)
        # self.x2 =  int(x + width)

    def test(self, player):
        if player.x < self.x1 or player.x > self.x2: return None
        if player.y <= self.y and player.y + player.velocity >= self.y: return self
        return None

    def draw(self,window):
        window.blit(self.image,(self.rect.x,self.rect.y))

    def redimensionne(self,width,height):
        self.image = pygame.transform.scale(self.image, (width,height))
