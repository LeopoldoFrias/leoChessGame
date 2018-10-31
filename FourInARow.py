import sys, pygame

pygame.init()

HEIGHT = 1260
WIDTH = 1260
chessBoard = pygame.image.load("ChessBoard.png")
pygame.display.set_caption("TXT Chess")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
click = pygame.key.get_pressed()
clock = pygame.time.Clock()

def Parameters():
    xMin = -30
    xMax = 600
    yMin = 30
    yMax = -600
    
piece = []

class Tile:
    pieceOnTile = None
    tileCoordinate = None

    def __init__(self, coordinate, piece):
        self.tileCoordinate = coordinate
        self.pieceOnTile = piece


class King(pygame.sprite.Sprite):

     alliance = None
     position = None

     def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('King:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.alliance = alliance
        self.rect.position = position
     def movement(self):
         self.movement = movement
         return "B" if self.alliance == "Black" else "b"
                 


class Queen(pygame.sprite.Sprite):

     alliance = None
     position = None

     def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('Queen black.jpg')
        self.rect = self.image.get_rect()
        self.rect.alliance = alliance
        self.rect.position = position
     def movement(self):
        self.movement = movement
        return "B" if self.alliance == "Black" else "b"




class Bishop(pygame.sprite.Sprite):

    alliance = None
    position = None

    def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('Bishop:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
    def movement(self):
         self.movement = movement
         return "B" if self.alliance == "Black" else "b"



class Castle(pygame.sprite.Sprite):

     alliance = None
     position = None

     def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('Castle:black.png')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
     def movement(self):
         self.movement = movement
         return "B" if self.alliance == "Black" else "b"


class Knight(pygame.sprite.Sprite):

     alliance = None
     position = None

     def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('Knight:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
     def movement(self):
        self.movement = movement
        return "B" if self.alliance == "Black" else "b"




class Pawn(pygame.sprite.Sprite):

    alliance = None
    position = None

    def __init__(self,alliance,position):
        super().__init__(self)
        self.movement = movement
        self.image = pygame.image.load('Pawn:black.jpg')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
    def movement(self):
        self.movement = movement
        return "B" if self.alliance == "Black" else "b"


class Board:

    boardTiles = {}
    def __init__(self):
        
        pass

    def creatBoard(self):

       for tile in range (64):
           self.creatBoard[tile] = Tile(tile())
            
            
    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('|', end=self.boardTiles[tiles].pieceOnTile.movement())
            count += 1
            if count == 8:
                print('|', end='\n')
                count = 0

     
while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()

   pygame.display.update()
   clock.tick(60)
   screen.blit(chessBoard())
   pygame.display.flip()

