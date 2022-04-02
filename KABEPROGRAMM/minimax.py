from cmath import inf
from kaik import possible_moves
from kaik import evaluation
from kabelaud import board_detection

def minimax(position, depth, max_player):
    if depth == 0:
        return evaluation(position), position

    if max_player:
        maxEval = float("-inf")
        best_move = None
        for move in possible_moves(position,"white"):
            evaluatn = minimax(move, depth-1, False)[0]
            maxEval = max(evaluatn, maxEval)
            if maxEval == evaluatn:
                best_move = move
        
        return maxEval, best_move
    
    else:
        minEval = float("inf")
        best_move = None
        for move in possible_moves(position,"black"):
            evaluatn = minimax(move, depth-1, True)[0]
            minEval = min(evaluatn, minEval)
            if minEval == evaluatn:
                best_move = move
        
        return minEval, best_move
