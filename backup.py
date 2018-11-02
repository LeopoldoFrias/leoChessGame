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


class Queen(pygame.sprite.Sprite):

    def __init__():
        super().__init__(self, pos)
        self.image = pygame.image.load('./images/Chess_tile_qd.png').convert()
        self.rect = self.image.get_rect()

class Bishop(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(self)
        self.image = pygame.image.load('.images/Chess_tile_bd.png').convert()
        self.rect = self.image.get_rect()


class Castle(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(self)
        self.image = pygame.image.load('.images/Chess_tile_rd.png').convert()
        self.rect = self.image.get_rect()

class Knight(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(self)
        self.image = pygame.image.load('.images/Chess_tile_nd.png').convert()
        self.rect = self.image.get_rect()

class Pawn(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__(self)
        self.image = pygame.image.load('./images/Chess_tile_pd.png').convert()
        self.rect = self.image.get_rect()
