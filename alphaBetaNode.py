from random import randint
import math

MIN = -math.inf
MAX = math.inf


class Node:
    def __init__(self, from_cell, to_here_cell, board, height):
        self.children = []
        self.utility = 0
        self.decisionChild = None
        self.from_cell = from_cell
        self.to_here_cell = to_here_cell
        self.board = board
        self.height = height

    def setChild(self, child):
        self.children.append(child)

    def setUtility(self, utility):
        self.utility = utility

    def setDecisionChild(self, decisionChild):
        self.decisionChild = decisionChild

    def getDecisionChild(self):
        return self.decisionChild

    def getFromCell(self):
        return self.from_cell

    def getToCell(self):
        return self.to_here_cell

    def a_b_setEvaluationFunction(self, color):
        evaluation = self.EvaluateArmy(color)
        self.utility = evaluation
        
    def setHeight(self, height):
        self.height = height
    
    def getHeight(self):
        return self.height

    def getUtility(self):
        return self.utility

    def winColor(self, color):
        opColor = 'W'        
        if color == 'W':
            opColor = 'B'

        if self.board.getNumberOfArmy(opColor) == 0:
            return True
 
        for i in range(self.board.n_cols):
            if color == 'B':
                if self.board.board[0][i] == color:
                    return True
            if color == 'W':
                if self.board.board[self.board.n_rows - 1][i] == color:
                    return True
        return False

    def EvaluateArmy(self, color):
        blackScore = 0 
        blackNum = 0
        whiteScore = 0
        whiteNum = 0

        for i in range(self.board.n_rows):
            for j in range(self.board.n_cols):
                
                if self.board.board[i][j] == 'W':
                    whiteNum +=1
                    if(i == (self.board.n_rows - 1)):
                        if(color == 'W'):
                            return MAX
                        else:
                            return MIN
                    posWeight = 1
                    for p in [-1, 0, 1]:
                        newj = j+p
                        if (newj == -1) or (newj == self.board.n_cols):
                            continue 
                        if self.board.board[i+1][newj] == 'E':
                            posWeight +=1
                    attacks = 0
                    for l in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        newi = i + l[0]
                        newj = j + l[1]
                        if (newj == -1) or (newj == self.board.n_cols):
                            continue
                        if (newi == -1) or (newi == self.board.n_rows):
                            continue
                        if self.board.board[newi][newj] == 'B':
                            attacks += 1
                    if(i > (self.board.n_rows - 3)):
                        whiteScore += (posWeight - attacks) * pow(i+1, 2)
                        
                    else:
                        whiteScore += (posWeight - attacks) * i+1

                
                if self.board.board[i][j] == 'B':
                    blackNum += 1
                    if(i == 0):
                        if(color == 'W'):
                            return MIN
                        else:
                            return MAX
                    posWeight = 1
                    for p in [-1, 0, 1]:
                        newj = j+p
                        if (newj == -1) or (newj == self.board.n_cols):
                            continue 
                        if self.board.board[i-1][newj] == 'E':
                            posWeight +=1
                    attacks = 0
                    for l in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                        newi = i + l[0]
                        newj = j + l[1]
                        if (newj == -1) or (newj == self.board.n_cols):
                            continue
                        if (newi == -1) or (newi == self.board.n_rows):
                            continue
                        if self.board.board[newi][newj] == 'W':
                            attacks += 1
                    if(i < 2):
                        blackScore += (posWeight - attacks) * pow(self.board.n_rows - i, 2)
                    else:
                        blackScore += (posWeight - attacks) * self.board.n_rows - i
     
        if(color == 'W'):
            if(blackNum == 0):
                return MAX
            if(whiteNum == 0):
                return MIN
            return whiteScore - 2 * blackScore
     
        else:
            if(blackNum == 0):
                return MIN
            if(whiteNum == 0):
                return MAX
            return blackScore - 2 * whiteScore