
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





