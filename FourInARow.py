import sys, pygame

pygame.init()

HEIGHT = 1260
WIDTH = 1260
pygame.display.set_caption("TXT Chess")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
click = pygame.key.get_pressed()
clock = pygame.time.Clock()

chessBoard = Board()
chessBoard.createBoard()
chessBoard.printBoard()

allPieces = []
allTiles = []

def squares(x, y, w, h, color):
    pygame.draw.rect(gameDisplay, color, [x,y,w,h])

def drawChessPieces():
    xpos = 0
    ypos = 0
    color = 0
    width = 100
    height = 100
    black = (0, 0, 0)
    white = (255, 255, 255)
    number = 0

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                squares(xpos, ypos, width, height, white)
                if not chessBoard.gameTiles[number].pieceOnTile.toString() == '-':
                    image = pygame.image.load("." + chessBoard.gameTiles[number].pieceOnTiles.alliance[0].upper()
                                              + chessBoard.gameTiles[number].pieceOnTile.toString.upper()
                                              + ".png")
                    image = pygame.transform.scale(image, (100,100))
                    allPieces.append([image, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTile])
                xpos += 100
            else:
                squares(xpos, ypos, width, height, black)
                if not chessBoard.gameTiles[number].pieceOnTile.toString() == '-':
                    image = pygame.image.load(""
                                              + chessBoard.gameTiles[number].pieceOnTiles.alliance[0].upper()
                                              + chessBoard.gameTiles[number].pieceOnTile.toString.upper()
                                              + ".png")
                    image = pygame.transform.scale(image (100,100))
                    allPieces.append([image, [xpos, ypos], chessBoard.gameTiles[number].pieceOnTiles])
                xpos += 100
            color += 1
            number += 1
        color += 1
        xpos = 0
        ypos += 100

                    # You have to add each other the sprite images ^
drawChessPieces()
piece = []

class NullPiece(piece):


    def __init__(self,alliance,position):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "-"


class Move:

    def __init__(self):
        pass

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
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.alliance = alliance
        self.rect.position = position

     def toString(self):
         return "B" if self.alliance == "Black" else "b"
                 


class Queen(pygame.sprite.Sprite):

     alliance = None
     position = None

     def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.alliance = alliance
        self.rect.position = position

     def toString(self):
        return "B" if self.alliance == "Black" else "b"


class Bishop(pygame.sprite.Sprite):

    alliance = None
    position = None

    def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
    def toString(self):
         return "B" if self.alliance == "Black" else "b"



class Castle(pygame.sprite.Sprite):

     alliance = None
     position = None

     def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
     def toString(self):
         return "B" if self.alliance == "Black" else "b"


class Knight(pygame.sprite.Sprite):

     alliance = None
     position = None

     def __init__(self,alliance,position):
        super().__init__(self)
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
     def toString(self):
        return "B" if self.alliance == "Black" else "b"


class Pawn(pygame.sprite.Sprite):

    alliance = None
    position = None

    def __init__(self,alliance,position):
        super().__init__(self)
        self.movement = movement
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
        self.rect.position = position
        self.rect.alliance = alliance
    def toString(self):
        return "B" if self.alliance == "Black" else "b"


class Board:

    boardTiles = {}
    enPassPawn = None
    enPassPawnBehind = None
    currentPlayer = "White"

    def __init__(self):
            pass

    def calculateActivePieces(self, alliance):

        activePiece = []
        for tile in range(len(self.boardTiles)):
            if not self.boardTiles[tile].pieceOnTile.alliance == alliance:
                activePiece.append(self.boardTiles[tile].pieceOnTile)

        return activePiece

    def calculateLegalMoves(self, pieces, board):

        allLegals = []

        for piece in pieces:
            pieceMoves = piece.calculateLegalMoves(board)
            for move in pieceMoves:
                allLegals.append([move, piece])
        return allLegals

    def creatBoard(self):

       for tile in range (64):
           self.boardTiles[0] = Tile(0, Castle("Black", 0))
           self.boardTiles[1] = Tile(1, Knight("Black", 1))
           self.boardTiles[2] = Tile(2, Bishop("Black", 2))
           self.boardTiles[3] = Tile(3, Queen("Black", 3))
           self.boardTiles[4] = Tile(4, King("Black", 4))
           self.boardTiles[5] = Tile(5, Bishop("Black", 5))
           self.boardTiles[6] = Tile(6, Knight("Black", 6))
           self.boardTiles[7] = Tile(7, Castle("Black", 7))
           self.boardTiles[8] = Tile(8, Pawn("Black", 8))
           self.boardTiles[9] = Tile(9, Pawn("Black", 9))
           self.boardTiles[10] = Tile(10, Pawn("Black", 10))
           self.boardTiles[11] = Tile(11, Pawn("Black", 11))
           self.boardTiles[12] = Tile(12, Pawn("Black", 12))
           self.boardTiles[13] = Tile(13, Pawn("Black", 13))
           self.boardTiles[14] = Tile(14, Pawn("Black", 14))
           self.boardTiles[15] = Tile(15, Pawn("Black", 15))
           self.boardTiles[48] = Tile(48, Pawn("White", 48))
           self.boardTiles[49] = Tile(49, Pawn("White", 49))
           self.boardTiles[50] = Tile(50, Pawn("White", 50))
           self.boardTiles[51] = Tile(51, Pawn("White", 51))
           self.boardTiles[52] = Tile(52, Pawn("White", 52))
           self.boardTiles[53] = Tile(53, Pawn("White", 53))
           self.boardTiles[54] = Tile(54, Pawn("White", 54))
           self.boardTiles[55] = Tile(55, Pawn("White", 55))
           self.boardTiles[56] = Tile(56, Castle("White", 56))
           self.boardTiles[57] = Tile(57, Knight("White", 57))
           self.boardTiles[58] = Tile(58, Bishop("White", 58))
           self.boardTiles[59] = Tile(59, Queen("White", 59))
           self.boardTiles[60] = Tile(60, King("White", 60))
           self.boardTiles[61] = Tile(61, Bishop("White", 61))
           self.boardTiles[62] = Tile(62, Knight("White", 62))
           self.boardTiles[63] = Tile(63, Castle("White", 63))
            
    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('|', end=self.boardTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('|', end='\n')
                count = 0
        for image in allPieces:
            gameDisplay.blit(image[0], image[1])

     
while 1:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()

   pygame.display.update()
   clock.tick(60)
   pygame.display.flip()