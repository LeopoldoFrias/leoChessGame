import sys, pygame, itertools

from pygame.locals import MOUSEBUTTONDOWN, MOUSEBUTTONUP
from MoreOfChess import Board as Board

pygame.init()

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


    def printBoard(self):
        count = 0
        for tiles in range(64):
            print('|', end=self.boardTiles[tiles].pieceOnTile.toString())
            count += 1
            if count == 8:
                print('|', end='\n')
                count = 0
        for image in allPieces:
            screen.blit(image[0], image[1])

            def game():
                # varibles will start of at their default state and will be changed under specific conditions
                SHOW_END_GAME = 1
                Mousedown = False
                Mousereleased = False
                TargetPiece = None
                checkmate = False
                check_message = False
                check = False
                teams = ['White', 'Black']
                colors = [dark_brown, light_brown]

                while True:
                    # While team 0's turn is true
                    turn = teams[0]
                    checkquitgame()
                    pieceholder = None

                    for piece in Pieces:
                        # checks condition if the king piece is in "check"
                        if type(piece) == King and piece.team == turn:
                            check = piece.undercheck()
                            if not check:
                                check_message = False
                            checkmate = piece.checkforcheckmate()
                    if checkmate:
                        # checkmate means the king can't be moved anywhere and the game will end
                        colors = [gray, violet]
                        drawboard(colors)
                        if SHOW_END_GAME:
                            show_checkmate(teams)
                            SHOW_END_GAME = 0
                    elif check and not check_message:
                        show_check(teams)
                        check_message = True
                        continue
                    drawboard(colors)
                    for event in pygame.event.get():
                        if event.type == MOUSEBUTTONDOWN:
                            Mousedown = True
                        if event.type == MOUSEBUTTONUP:
                            Mousedown = False
                            Mousereleased = True

                    # get cursor
                    Cursor = pygame.mouse.get_pos()
                    if Mousedown and not TargetPiece:
                        TargetPiece = nearest_piece(Cursor, Pieces)
                        if TargetPiece:
                            OriginalPlace = TargetPiece.square
                    if Mousedown and TargetPiece:
                        TargetPiece.drag(Cursor)
                    if Mousereleased:
                        Mousereleased = False
                        if TargetPiece and TargetPiece.team != turn:  # check your turn
                            TargetPiece.update(OriginalPlace)
                            TargetPiece = None
                        elif TargetPiece:
                            pos1 = TargetPiece.rect.center
                            for Square in squareCenters:
                                if distance_formula(pos1, Square.center) < BoardWidth / 16:  # half width of square
                                    newspot = Square
                                    otherpiece = nearest_piece(Square.center, Pieces)
                                    break
                                # if otherpiece and otherpiece != TargetPiece and otherpiece.team == TargetPiece.team:
                                TargetPiece.update(OriginalPlace)
                                # elif newspot not in TargetPiece.movelist():
                                TargetPiece.update(OriginalPlace)
                                # elif otherpiece and otherpiece != TargetPiece and type(otherpiece) != King:
                                for piece in Pieces:
                                    if piece == otherpiece:
                                        pieceholder = piece
                                        Pieces.remove(piece)
                                        TargetPiece.update(newspot)
                                teams = teams[::-1]  # switch teams
                            else:
                                TargetPiece.update(newspot)
                                if type(TargetPiece) == Pawn or type(TargetPiece) == BlackPawn or type(
                                        TargetPiece) == King:
                                    TargetPiece.bool += 1
                                teams = teams[::-1]
                            if True:
                                check = False
                                for piece in Pieces:
                                    if type(piece) == King and piece.team == turn:
                                        check = piece.undercheck()
                            if check:
                                TargetPiece.update(OriginalPlace)
                                if pieceholder and pieceholder.team != TargetPiece.team:
                                    Pieces.append(pieceholder)
                                    pieceholder = None
                                teams = teams[::-1]
                            TargetPiece = None

                        for piece in Pieces:
                            piece.draw(screen)
                        pygame.display.flip()


class NullPiece():
    def __init__(self):
        pass


class Tile:

    def __init__(self, pos):
        self.tileCoordinate = coordinate
        self.pieceOnTile = piece


# Sprites = pygame.Surface((100, 100))

# simple variables
pygame.display.set_caption("TXT Chess")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

piece = []


# ------------------------------------------------------------------------------------------------------------------
# What conditions will be if their is not piece present at that time

class BlackKing(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_kd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))
       self.screen.blit(self.bigger_img)


class BlackBishop(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_bd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class BlackKnight(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_nd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class BlackPawn(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class BlackCastle(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_rd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class BlackQueen(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_qd.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()
        self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class WhiteKing(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_kl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()
        self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class WhiteQueen(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_ql.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()
        self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class WhiteCastle(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_rl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()
        self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class WhiteKnight(pygame.sprite.Sprite):

    def __init__(self, pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_nl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class WhiteBishop(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_bl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))

class WhitePawn(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()
       self.bigger_img = pygame.transform.scale(self.image, (int(self.size[0] * 2), int(self.size[1] * 2)))


# ------------------------------------------------------------------------------------------------------------
# Create pieces

whiteTeam = pygame.sprite.Group()
blackTeam = pygame.sprite.Group()
#positions
blackking = BlackKing([100, 100])
blackqueen = BlackQueen([100, 100])
blackcastle = BlackCastle([100, 100])
blackknight = BlackKnight([100, 100])
blackpawn = BlackPawn([100, 100])
blackbishop = BlackBishop([100, 100])
blackTeam.add(blackking, blackqueen, blackcastle, blackknight, blackpawn, blackbishop)

whiteking = WhiteKing([100, 100])
whitequeen = WhiteQueen([100, 100])
whitecastle = WhiteCastle([100, 100])
whiteknight = WhiteKnight([100, 100])
whitepawn = WhitePawn([100, 100])
whitebishop = WhiteBishop([100, 100])
whiteTeam.add(whiteking, whitequeen, whitecastle, whiteknight, whitepawn, whitebishop)


# Constantly active variables during run time
while 1:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           sys.exit()


# The screen display is being "drawn" (updated) to show board and pieces
    screen.fill((60, 70, 90))
    screen.blit(background, (100, 100))

    whiteTeam.draw(screen)
    blackTeam.draw(screen)
    pygame.display.update()
    pygame.display.update()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
