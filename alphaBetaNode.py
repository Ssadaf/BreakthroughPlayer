from random import randint


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

    def setEvaluationFunction(self, color):
        evaluation = self.board.EvaluateArmy(color)
        self.utility = evaluation
        
    def setHeight(self, height):
        self.height = height
    
    def getHeight(self):
        return self.height

    def getUtility(self):
        return self.utility