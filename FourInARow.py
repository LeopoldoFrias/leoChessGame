import sys, pygame, itertools, PySimpleGUI

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

mouseClick = pygame.mouse.get_pressed()

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

class BlackBishop(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_bd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackBishop2(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_bd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()


class BlackKnight(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_nd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackKnight2(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_nd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackPawn(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackPawn2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackPawn3(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackPawn4(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackPawn5(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackPawn6(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackPawn7(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()


class BlackCastle(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_rd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class BlackCastle2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_rd.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()


class BlackQueen(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_qd.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()

class WhiteKing(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_kl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()

class WhiteQueen(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_ql.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()

class WhiteCastle(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_rl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()

class WhiteCastle2(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.image = pygame.image.load("./images/Chess_tile_rl.png")
        self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
        self.size = self.image.get_size()


class WhiteKnight(pygame.sprite.Sprite):

    def __init__(self, pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_nl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhiteKnight2(pygame.sprite.Sprite):

    def __init__(self, pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_nl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhiteBishop(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_bl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhiteBishop2(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_bl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhitePawn(pygame.sprite.Sprite):

   def __init__(self,pos):
       super().__init__()
       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhitePawn2(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhitePawn3(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhitePawn4(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhitePawn5(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhitePawn6(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()

class WhitePawn7(pygame.sprite.Sprite):

   def __init__(self,pos):

       super().__init__()

       self.image = pygame.image.load("./images/Chess_tile_pl.png")
       self.rect = pygame.Rect(pos[0], pos[0], 10, 10)
       self.size = self.image.get_size()


# ------------------------------------------------------------------------------------------------------------
# Create pieces


whiteTeam = pygame.sprite.Group()
blackTeam = pygame.sprite.Group()
#positions
blackking = BlackKing([655, -800])
blackqueen = BlackQueen([230, 100])
blackcastle = BlackCastle([100, 100])
blackknight = BlackKnight([100, 100])
blackpawn = BlackPawn([600, 600])
blackbishop = BlackBishop([500, 500])

blackcastle2 = BlackCastle2([100, 100])
blackbishop2 = BlackBishop2([100, 100])
blackknight2 = BlackKnight2([100, 100])

blackpawn2 = BlackPawn2([100, 100])
blackpawn3 = BlackPawn3([100, 100])
blackpawn4 = BlackPawn4([100, 100])
blackpawn5 = BlackPawn5([100, 100])
blackpawn6 = BlackPawn6([100, 100])
blackpawn7 = BlackPawn7([100, 100])
blackTeam.add(blackking, blackqueen, blackcastle, blackknight, blackpawn, blackbishop, blackpawn2,
              blackpawn3, blackpawn4, blackpawn5, blackpawn6, blackpawn7, blackbishop2, blackcastle2, blackknight2)

whiteking = WhiteKing([100, 100])
whitequeen = WhiteQueen([100, 100])
whitecastle = WhiteCastle([100, 100])
whiteknight = WhiteKnight([180, 180])
whitepawn = WhitePawn([200, 50])
whitebishop = WhiteBishop([100, 100])

whitecastle2 = WhiteCastle2([100, 100])
whiteknight2 = WhiteKnight2([100, 100])
whitebishop2 = WhiteBishop2([100, 100])

whitepawn2 = WhitePawn2([100, 100])
whitepawn3 = WhitePawn3([100, 100])
whitepawn4 = WhitePawn4([100, 100])
whitepawn5 = WhitePawn5([100, 100])
whitepawn6 = WhitePawn6([100, 100])
whitepawn7 = WhitePawn7([100, 100])
whiteTeam.add(whiteking, whitequeen, whitecastle, whiteknight, whitepawn, whitebishop, whitepawn2,
              whitepawn3, whitepawn4, whitepawn5, whitepawn6, whitepawn7, whitebishop2, whitecastle2, whiteknight2)


# def Render(self, screen):
#     pygame.draw.circle(screen, self.color, self.pos, self.size)
#
#
# def main():  # Where we start
#     screen = pygame.display.set_mode((600, 400))
#
#
# running = True
# RenderList = []  # list of objects
# MousePressed = False  # Pressed down THIS FRAME
# MouseDown = False  # mouse is held down
# MouseReleased = False  # Released THIS FRAME
# Target = None  # target of Drag/Drop
# while running:
#     screen.fill((0, 0, 0))  # clear screen
# pos = pygame.mouse.get_pos()
# for Event in pygame.event.get():
#     if Event.type == pygame.QUIT:
#         running = False
# #break   get out now
#
# if Event.type == pygame.MOUSEBUTTONDOWN:
#     MousePressed = True
# MouseDown = True
#
# if Event.type == pygame.MOUSEBUTTONUP:
#     MouseReleased = True
# MouseDown = False
#
# if MousePressed == True:
#     for item in RenderList:  # search all items
#         if (pos[0] >= (item.pos[0] - item.size) and
#                 pos[0] <= (item.pos[0] + item.size) and
#                 pos[1] >= (item.pos[1] - item.size) and
#                 pos[1] <= (item.pos[1] + item.size)):  # inside the bounding box
#             print('okay')
#         # Target = whiteTeam, blackTeam # "pick up" item
#
# if blackTeam is None:  # didn't find any?
#     blackTeam = Disk((0, 0, 255), pos, 10)  # create a new one
# RenderList.append(blackTeam)  # add to list of things to draw
#
# if MouseDown and blackTeam is not None:  # if we are dragging something
#     blackTeam.pos = pos  # move the target with us
#
# if MouseReleased:
#     blackTeam = None  # Drop item, if we have any
#
# for blackTeam in RenderList:
#     blackTeam.Render(screen)  # Draw all items
#
# MousePressed = False  # Reset these to False
# MouseReleased = False  # Ditto

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