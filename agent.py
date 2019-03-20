from alphaBeta import AlphaBeta
from alphaBetaTree import Tree
import time

class Agent:
    def __init__(self, color, opponentColor, time=None):
        self.myColor = color
        self.opponentColor = opponentColor
        self.height = 5


    def move(self, board):
        startTime = time.time()
        gameTree = Tree(board, self.height, self.myColor, self.opponentColor)
        from_cell, to_cell = AlphaBeta.a_b_calNextMove(gameTree)
        elapsedTime = time.time() - startTime
        print(elapsedTime)
        return from_cell, to_cell
