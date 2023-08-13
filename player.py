class Player():
    def __init__(self, number, pieces):
        self.number = number
        self.inCheck = False
        self.pieces = pieces
        self.king = None

    def isInCheck(self):
        return self.king.isInCheck()