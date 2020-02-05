import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        #Gere la hauteur du saut
        self.hauteurSaut = 10
        self.oxygeneMax = 100
        self.oxygene = 100
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = self.hauteurSaut
        self.left = False
        self.right = False
        self.walkCount = 0
        cheminImage = "images/player/"
        self.walkRight = [
            pygame.image.load(cheminImage+'R1.png'),
            pygame.image.load(cheminImage+'R2.png'),
            pygame.image.load(cheminImage+'R3.png'),
            pygame.image.load(cheminImage+'R4.png'),
            pygame.image.load(cheminImage+'R5.png'),
            pygame.image.load(cheminImage+'R6.png'),
            pygame.image.load(cheminImage+'R7.png'),
            pygame.image.load(cheminImage+'R8.png'),
            pygame.image.load(cheminImage+'R9.png')
        ]
        self.walkLeft = [
            pygame.image.load(cheminImage+'L1.png'),
            pygame.image.load(cheminImage+'L2.png'),
            pygame.image.load(cheminImage+'L3.png'),
            pygame.image.load(cheminImage+'L4.png'),
            pygame.image.load(cheminImage+'L5.png'),
            pygame.image.load(cheminImage+'L6.png'),
            pygame.image.load(cheminImage+'L7.png'),
            pygame.image.load(cheminImage+'L8.png'),
            pygame.image.load(cheminImage+'L9.png')
        ]
        self.char = pygame.image.load(cheminImage+'standing.png')
    def draw(self,window):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            window.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(self.char, (self.x,self.y))

    def move_left(self):
        #délacement gauche
        self.x -= self.velocity
        self.left = True
        self.right = False

    def move_right(self):
        #deplacement droite
        self.x += self.velocity
        self.left = False
        self.right = True

    def no_move(self):
        self.right = False
        self.left = False
        self.walkCount = 0

    def jump(self):
        self.isJump = True
        self.right = False
        self.left = False
        self.walkCount = 0

    def doJump(self):
        if self.jumpCount >= 0:
            self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10
