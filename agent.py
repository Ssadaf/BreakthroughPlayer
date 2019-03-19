from alphaBeta import AlphaBeta
from alphaBetaTree import Tree

class Agent:
    def __init__(self, color, opponentColor, time=None):
        self.myColor = color
        self.opponentColor = opponentColor
        self.height = 4


    def move(self, board):
        gameTree = Tree(board, self.height, self.myColor, self.opponentColor)
        from_cell, to_cell = AlphaBeta.calNextMove(gameTree)
        return from_cell, to_cell
