import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        #Gere la hauteur du saut
        self.hauteurSaut = 10
        self.oxygene = 50
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 15
        self.xVelocity = 0
        self.isJump = False
        self.jumpCount = 0 #self.hauteurSaut
        self.left = False
        self.right = False
        self.walkCount = 0
        self.falling = True
        self.currentPlatform = None
        self.maxJumpRange = self.hauteurSaut
        self.jumping = False



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

    def keys(self):

        k = pygame.key.get_pressed()
        if k[pygame.K_LEFT]:
            self.x -=self.velocity
            self.right = False
            self.left = True

        elif k[pygame.K_RIGHT]:
            self.x += self.velocity
            self.right = True
            self.left = False

        else:
            self.right = False
            self.left = False

        if k[pygame.K_SPACE] and not self.falling:
            self.jumping = True
            self.jumpCounter = 0

    # def test(self):
    #     if player.x < self.x1 or player.x > self.x2:
    #         return None
    #     if player.y <= self.y and player.y + player.velocity >= self.y:
    #         return self
    #     return True

    def move(self):

        if self.currentPlatform:
            if not self.currentPlatform.test(self):
                self.falling = True
                self.currentPlatform = None
        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            self.y += self.velocity

    #gere les evenements du joueurs
    def do(self):
        self.keys()
        self.move()


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
        if self.jumpCount >= -self.hauteurSaut:
            self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10

    # class platform:
    # 	def __init__(self, x, y, width):
    # 		self.x1 = int(x)
    # 		self.y = int(y)
    # 		self.x2 =  int(x + width)
    #
    # 	def test(self, player):
    # 		if player.x < self.x1 or player.x > self.x2: return None
    # 		if player.y <= self.y and player.y + player.velocity >= self.y: return self
    # 		return None

    # class platforms:
    # 	def __init__(self):
    # 		self.container = list([])
    #
    # 	def add(self, p):
    # 		self.container.append(p)

    	# def testCollision(self, player):
    	# 	if not player.falling: return False
    	# 	for p in self.container:
    	# 		result = p.test(player)
    	# 		if result:
    	# 			player.currentPlatform = result
    	# 			player.y = result.y
    	# 			player.falling = False
    	# 			return True
    	# 	return False
        #
    	# def draw(self):
    	# 	WHITE = (0, 255, 0, 255)
    	# 	display = pygame.display.get_surface()
    	# 	for p in self.container:
    	# 		pygame.draw.line(display, WHITE, (p.x1, p.y), (p.x2, p.y), 10)

    	# def do(self, player):
    	# 	self.testCollision(player)
    	# 	self.draw()
