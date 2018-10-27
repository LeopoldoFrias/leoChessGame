import sys, pygame

pygame.init()

HEIGHT = 1260
WIDTH = 1260
chessBoard = pygame.image.load("ChessBoard.png")
pygame.display.set_caption("TXT Chess")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
click = pygame.key.get_pressed()

class King(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.image = pygame.image.load('King:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def movement(self):
        if click[pygame.K_6]:


class Queen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.image = pygame.image.load('Queen black.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def movement(self):
        if click[pygame.K_5]:



class Bishop(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.image = pygame.image.load('Bishop:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def movement(self):
        if click[pygame.K_4]:


class Castle(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.image = pygame.image.load('Castle:black.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def movement(self):
        if click[pygame.K_3]:

class Knight(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.image = pygame.image.load('Knight:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def movement(self):
        if click[pygame.K_2]:

class Pawn(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__(self)
        self.image = pygame.image.load('Pawn:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def movement(self):
        if click[pygame.K_1]:

while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()

   pygame.display.flip()

