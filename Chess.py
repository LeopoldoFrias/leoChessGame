import sys, pygame, itertools # from Chessnut import Game
pygame.init()

#chessgame = Game()  # Initialize a game in the standard opening position

HEIGHT = 900
WIDTH = 840
BLACK = pygame.Color('grey')
WHITE = pygame.Color('blue')

# This is where the chess board is actually being made
colors = itertools.cycle((WHITE, BLACK))
tile_size = 80
width, height = 8*tile_size, 8*tile_size
background = pygame.Surface((width, height))
for y in range(0, height, tile_size):
    for x in range(0, width, tile_size):
        rect = (x, y, tile_size, tile_size)
        pygame.draw.rect(background, next(colors), rect)
    next(colors)

pygame.display.set_caption("UltimateChess")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
mouseClick = pygame.mouse.get_pressed()

# ------------------------------------------------------------------------------------------------------------------
""" This is all the classes for each individual piece. Each class has a specific sprite,
    based on its image, and it's own invisible rectangle."""

class BlackKing(pygame.sprite.Sprite):

   def __init__(self, pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_kd.png")
       self.rect = pygame.Rect(pos[1], pos[-1], 1, 1)
       self.rect = self.image.get_rect()

class BlackBishop(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_bd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackBishop2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_bd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackKnight(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_nd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackKnight2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_nd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackPawn(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackPawn2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackPawn3(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackPawn4(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackPawn5(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackPawn6(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackPawn7(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackCastle(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_rd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackCastle2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_rd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class BlackQueen(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./images/Chess_tile_qd.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.rect = self.image.get_rect()

class WhiteKing(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./images/Chess_tile_kl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.rect = self.image.get_rect()

class WhiteQueen(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./images/Chess_tile_ql.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.rect = self.image.get_rect()

class WhiteCastle(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./images/Chess_tile_rl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.rect = self.image.get_rect()

class WhiteCastle2(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("./images/Chess_tile_rl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.rect = self.image.get_rect()

class WhiteKnight(pygame.sprite.Sprite):

    def __init__(self, pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_nl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhiteKnight2(pygame.sprite.Sprite):

    def __init__(self, pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_nl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhiteBishop(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_bl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhiteBishop2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_bl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhitePawn(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhitePawn2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhitePawn3(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhitePawn4(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhitePawn5(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhitePawn6(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

class WhitePawn7(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.rect = self.image.get_rect()

# ------------------------------------------------------------------------------------------------------------
# Reassigning the class to new variables to set those new variables  all in a class
whiteTeam = pygame.sprite.Group()
blackTeam = pygame.sprite.Group()

blackking = BlackKing([655, -800])
blackqueen = BlackQueen([230, 100])
blackcastle = BlackCastle([100, 100])
blackknight = BlackKnight([100, 100])
blackpawn = BlackPawn([600, 600])
blackbishop = BlackBishop([500, 500])

blackcastle2 = BlackCastle2([100, 100])
blackbishop2 = BlackBishop2([190, 100])
blackknight2 = BlackKnight2([100, 100])

blackpawn2 = BlackPawn2([-340, 100])
blackpawn3 = BlackPawn3([100, 100])
blackpawn4 = BlackPawn4([90, 100])
blackpawn5 = BlackPawn5([100, 100])
blackpawn6 = BlackPawn6([100, 100])
blackpawn7 = BlackPawn7([120, 100])
blackTeam.add(blackking, blackqueen, blackcastle, blackknight, blackpawn, blackbishop, blackpawn2,
              blackpawn3, blackpawn4, blackpawn5, blackpawn6, blackpawn7, blackbishop2, blackcastle2, blackknight2)

whiteking = WhiteKing([100, 100])
whitequeen = WhiteQueen([100, 100])
whitecastle = WhiteCastle([100, 100])
whiteknight = WhiteKnight([180, 180])
whitepawn = WhitePawn([200, 50])
whitebishop = WhiteBishop([100, 100])

whitecastle2 = WhiteCastle2([129, 230])
whiteknight2 = WhiteKnight2([320, 100])
whitebishop2 = WhiteBishop2([321, 100])

whitepawn2 = WhitePawn2([432, 532])
whitepawn3 = WhitePawn3([234, 103])
whitepawn4 = WhitePawn4([423, 289])
whitepawn5 = WhitePawn5([123, 345])
whitepawn6 = WhitePawn6([987, 203])
whitepawn7 = WhitePawn7([299, 100])
whiteTeam.add(whiteking, whitequeen, whitecastle, whiteknight, whitepawn, whitebishop, whitepawn2,
              whitepawn3, whitepawn4, whitepawn5, whitepawn6, whitepawn7, whitebishop2, whitecastle2, whiteknight2)

while 1:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()

    all_sprites = blackTeam, whiteTeam
    all_sprites.update()

    Eat = pygame.sprite.groupcollide(all_sprites, True)
\
    screen.fill((60, 70, 90))
    # The background color ^
    screen.blit(background, (100, 100))
    # Displays background
    false = blackking.kill()

    whiteTeam.draw(screen)
    blackTeam.draw(screen)
    # Draws the sprite groups on the screen
    pygame.display.update()
    clock.tick(60)
    # fps
    pygame.display.flip()

pygame.quit()