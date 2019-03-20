from random import randint
import math

MIN = -math.inf
MAX = math.inf

class Node:
    def __init__(self, from_cell, to_here_cell, board):
        self.children = []
        self.utility = 0
        self.decisionChild = None
        self.from_cell = from_cell
        self.to_here_cell = to_here_cell
        self.board = board

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

    def setEvaluationFunction(self):
        evaluation = randint(-100, 100)
        # evaluation = self.EvaluateArmy('B')
        self.utility = evaluation

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
                            # print("1111->", i)
                            return MAX
                        else:
                            return MIN
                    if(i > (self.board.n_rows - 3)):
                        whiteScore += pow(i+1, 2)
                    else:
                        whiteScore += i+1

                
                if self.board.board[i][j] == 'B':
                    blackNum += 1
                    if(i == 0):
                        if(color == 'W'):
                            return MIN
                        else:
                            # print("2222")
                            return MAX
                    if(i < 2):
                        blackScore += pow(self.board.n_rows - i, 2)
                    else:
                        blackScore += self.board.n_rows - i
     
        if(color == 'W'):
            if(blackNum == 0):
                # print("3333")
                return MAX
            if(whiteNum == 0):
                return MIN
            return whiteScore - 2*blackScore
     
        else:
            if(blackNum == 0):
                return MIN
            if(whiteNum == 0):
                # print("4444")
                return MAX
            return blackScore - 2*whiteScore