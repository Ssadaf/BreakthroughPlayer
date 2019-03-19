import math

MIN = -math.inf
MAX = math.inf

class AlphaBeta:
    @staticmethod
    def calNextMove(tree):
        decistionNode = tree.root.getDecisionChild()
        return decistionNode.getFromCell(), decistionNode.getToCell()




#     def alpha_beta_search(self, tree, depth):
#         best_val = MIN
#         beta = MAX

#         if(depth == 0):

#         successors = self.getSuccessors(node)
#         decisionNode = None
#             if len(father.children) > 0:
#                 for child in father.children:
#         #####
#             value = self.min_value(state, best_val, beta)
#             if value > best_val:
#                 best_val = value
#                 best_state = state
#         print "AlphaBeta:  Utility Value of Root Node: = " + str(best_val)
#         print "AlphaBeta:  Best State is: " + best_state.Name
#         return best_state

#     def a_b_minimax(self, node, depth, minTillNow, maxTillNow, isMax):
#         if(depth == 0):
#             node.setEvaluationFunction()
#         if isMax:
#             best_val = minTillNow
            
#             decisionNode = None
#             if len(node.children) > 0:
#                 for child in node.children:
#                     val = a_b_minimax(child, depth-1, best_val, maxTillNow, False)
#                     if val > best_val:
#                         best_val = val
#                         decisionNode = child
#         else:
#             best_val = maxTillNow

#             decisionNode = None
#             if len(node.children) > 0:
#                 for child in node.children:
#                     val = a_b_minimax(child, depth-1, minTillNow, best_val, True)
#                     if val > best_val:
#                         best_val = val
#                         decisionNode = child

#         father.setUtility(best_val)
#         father.setDecisionChild(decisionNode)
            



#     def max_value(self, node, alpha, beta):
#         print "AlphaBeta-->MAX: Visited Node :: " + node.Name
#         if self.isTerminal(node):
#             return self.getUtility(node)
#         infinity = float('inf')
#         value = -infinity

#         successors = self.getSuccessors(node)
#         for state in successors:
#             value = max(value, self.min_value(state, alpha, beta))
#             if value >= beta:
#                 return value
#             alpha = max(alpha, value)
#         return value

#     def min_value(self, node, alpha, beta):
#         print "AlphaBeta-->MIN: Visited Node :: " + node.Name
#         if self.isTerminal(node):
#             return self.getUtility(node)
#         infinity = float('inf')
#         value = infinity

#         successors = self.getSuccessors(node)
#         for state in successors:
#             value = min(value, self.max_value(state, alpha, beta))
#             if value <= alpha:
#                 return value
#             beta = min(beta, value)

#         return value
# ########################################

    # @staticmethod
    # def calNextMove(tree, height):
    #     AlphaBeta.computeEvaluationFunction(tree, height)
    #     AlphaBeta.computeAlphaBetaValueNodes(tree, height)
    #     decistionNode = tree.root.getDecisionChild()
    #     return decistionNode.getFromCell(), decistionNode.getToCell()

    # @staticmethod
    # def computeAlphaBetaValueNodes(tree, height):
    #     isMax = True
    
    #     if not isMax: #min node
    #         AlphaBeta.chooseDecistionChild(False, i-1, math.inf, tree)
    #         isMax = True
    #     else:
    #         AlphaBeta.chooseDecistionChild(True, i-1, -math.inf, tree)
    #         isMax = False

    # @staticmethod
    # def chooseDecistionChild(isMax, i, maxMinValue, tree):
    #     for j in range(len(tree.nodes[i])):
    #         father = tree.nodes[i][j]
    #         maxMinUtility = maxMinValue
    #         decisionNode = None
    #         if len(father.children) > 0:
    #             for child in father.children:
    #                 if not isMax:
    #                     if child.utility < maxMinUtility:
    #                         maxMinUtility = child.utility
    #                         decisionNode = child
    #                 if isMax:
    #                     if child.utility > maxMinUtility:
    #                         maxMinUtility = child.utility
    #                         decisionNode = child
    #             father.setUtility(maxMinUtility)
    #             father.setDecisionChild(decisionNode)

    # @staticmethod
    # def computeEvaluationFunction(tree, height):
    #     for leaf in tree.nodes[height]:
    #         leaf.setEvaluationFunction()
