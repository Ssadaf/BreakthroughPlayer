import copy
from alphaBetaNode import Node
import math

MIN = -math.inf
MAX = math.inf

class Tree:
    def __init__(self, board, height, color, opponentColor):
        self.height = height
        self.board = board
        self.nodes = [[] for i in range(self.height+1)]
        self.root = self.makeNode(0, board)
        self.buildTree(color, opponentColor)

    def makeNode(self, height, board, from_cell=None, to_cell=None):
        node = Node(from_cell, to_cell, board, height)
        self.nodes[height].append(node)
        return node

    def buildTree(self, color, opponentColor):
        self.evaluateNode(self.root, True, color, opponentColor, MIN, MAX)

    def evaluateNode(self, node, maxTurn, color, opponentColor, alpha, beta):
        if node.board.win(color) or node.board.win(opponentColor) or (node.getHeight() == self.height):
            node.setEvaluationFunction(color)

            # print("leaf", node.getUtility())
            
            return node.getUtility()    

        else:
        # print("##############")

            decisionNode = None
            bestVal = 0
            if maxTurn:
                bestVal = MIN
                piecesFromCell, piecesToCell = node.board.getPiecesPossibleLocations(color)
                shouldPrune = False
                for i in range(len(piecesToCell)):
                    if shouldPrune:
                        break
                    for j in range(len(piecesToCell[i])):
                        newBoard = copy.deepcopy(node.board)
                        newBoard.changePieceLocation(color, piecesFromCell[i], piecesToCell[i][j])

                        childNode = self.makeNode(node.getHeight()+1, newBoard, piecesFromCell[i], piecesToCell[i][j])

                        node.setChild(childNode)
                        value = self.evaluateNode(childNode, False, opponentColor, color, alpha, beta)
                        if value > bestVal:
                            bestVal = value
                            decisionNode = childNode
                        alpha = max(alpha, bestVal)
                        if beta <= alpha:
                            shouldPrune = True
                            break
            else:
                bestVal = MAX
                piecesFromCell, piecesToCell = node.board.getPiecesPossibleLocations(opponentColor)
                shouldPrune = False
                for i in range(len(piecesToCell)):
                    for j in range(len(piecesToCell[i])):
                        newBoard = copy.deepcopy(node.board)
                        newBoard.changePieceLocation(opponentColor, piecesFromCell[i], piecesToCell[i][j])

                        childNode = self.makeNode(node.getHeight()+1, newBoard, piecesFromCell[i], piecesToCell[i][j])

                        node.setChild(childNode)
                        value = self.evaluateNode(childNode, True, color, opponentColor, alpha, beta)
                        if value < bestVal:
                            bestVal = value
                            decisionNode = childNode
                        beta = min(beta, bestVal)
                        if beta <= alpha:
                            shouldPrune = True
                            break    
            node.setUtility(bestVal)
            node.setDecisionChild(decisionNode)
            # print("final: ",bestVal)
            # print("##############")
            return bestVal 
