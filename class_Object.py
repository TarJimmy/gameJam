import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,cheminImage, type = "object"):
        super().__init__()
        self.image = pygame.image.load(cheminImage)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = 30
        self.height = 40
        self.type = type
        self.x1 = x - self.width
        self.x2 =  x + self.height
        self.y = y - 41
        self.end = False
        # self.x1 = int(x)
        # self.y = int(y)
        # self.x2 =  int(x + width)

    def test(self, player):
        if player.x < self.x1 or player.x > self.x2: return None
        if player.y <= self.y and player.y + player.velocity >= self.y: return self
        return None

    def draw(self,window):
        if not self.end:
            window.blit(self.image,(self.rect.x,self.rect.y))

    def redimensionne(self,width,height):
        self.image = pygame.transform.scale(self.image, (width,height))
