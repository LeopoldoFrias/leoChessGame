
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

        for tile in range(64):
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

