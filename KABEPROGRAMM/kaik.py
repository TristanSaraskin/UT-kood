from copy import deepcopy
from kabelaud import board_detection

def possible_moves(situation, color):
    future_boards = []
    pieces = []

    for col in range(8):
        for row in range(8):
            if type(situation[col][row]) == list:
                pieces += [situation[col][row]]

    if color == "white":
        for piece in pieces:
            if piece[2] == 0: #Kui on valge
            
                if 0 <= piece[0]+1 <= 7 and 0 <= piece[1]+1 <= 7:
                    if situation[piece[0]+1][piece[1]+1] == 0: #Kui on tuhi koht
                        temp_situation = deepcopy(situation)
                        temp_situation[piece[0]][piece[1]] = 0
                        temp_situation[piece[0]+1][piece[1]+1] = [piece[0]+1, piece[1]+1, 0]
                        future_boards += [temp_situation] #lisab laua voimalike laudade listi

                    if type(situation[piece[0]+1][piece[1]+1]) == list: #kui on nupp
                        if situation[piece[0]+1][piece[1]+1][2] == 1: #Kui on tais koht ja vastaskabend
                            if 0 <= piece[0]+2 <= 7 and 0 <= piece[1]+2 <= 7:
                                if situation[piece[0]+2][piece[1]+2] == 0: #Kui taga on tuhi
                                    temp_situation = deepcopy(situation)
                                    temp_situation[piece[0]][piece[1]] = 0
                                    temp_situation[piece[0]+1][piece[1]+1] = 0
                                    temp_situation[piece[0]+2][piece[1]+2] = [piece[0]+2, piece[1]+2, 0]
                                    future_boards += [temp_situation] #lisab laua voimalike laudade listi

                if 0 <= piece[0]-1 <= 7 and 0 <= piece[1]+1 <= 7:
                    if situation[piece[0]-1][piece[1]+1] == 0: #Kui on tuhi koht
                        temp_situation = deepcopy(situation)
                        temp_situation[piece[0]][piece[1]] = 0
                        temp_situation[piece[0]-1][piece[1]+1] = [piece[0]-1, piece[1]+1, 0]
                        future_boards += [temp_situation] #lisab laua voimalike laudade listi

                    if type(situation[piece[0]-1][piece[1]+1]) == list: #Kui on nupp
                        if situation[piece[0]-1][piece[1]+1][2] == 1: #Kui on tais koht ja vastaskabend
                            if 0 <= piece[0]-2 <= 7 and 0 <= piece[1]+2 <= 7:
                                if situation[piece[0]-2][piece[1]+2] == 0: #Kui taga on tuhi
                                    temp_situation = deepcopy(situation)
                                    temp_situation[piece[0]][piece[1]] = 0
                                    temp_situation[piece[0]-1][piece[1]+1] = 0
                                    temp_situation[piece[0]-2][piece[1]+2] = [piece[0]-2, piece[1]+2, 0]
                                    future_boards += [temp_situation] #lisab laua voimalike laudade listi

    if color == "black":
        for piece in pieces:
            if piece[2] == 1: #Kui on must
            
                if 0 <= piece[0]+1 <= 7 and 0 <= piece[1]-1 <= 7:
                    if situation[piece[0]+1][piece[1]-1] == 0: #Kui on tuhi koht
                        temp_situation = deepcopy(situation)
                        temp_situation[piece[0]][piece[1]] = 0
                        temp_situation[piece[0]+1][piece[1]-1] = [piece[0]+1, piece[1]-1, 1]
                        future_boards += [temp_situation] #lisab laua voimalike laudade listi

                    if type(situation[piece[0]+1][piece[1]-1]) == list: #kui on nupp
                        if situation[piece[0]+1][piece[1]-1][2] == 0: #Kui on tais koht ja vastaskabend
                            if 0 <= piece[0]+2 <= 7 and 0 <= piece[1]-2 <= 7:
                                if situation[piece[0]+2][piece[1]-2] == 0: #Kui taga on tuhi
                                    temp_situation = deepcopy(situation)
                                    temp_situation[piece[0]][piece[1]] = 0
                                    temp_situation[piece[0]+1][piece[1]-1] = 0
                                    temp_situation[piece[0]+2][piece[1]-2] = [piece[0]+2, piece[1]-2, 1]
                                    future_boards += [temp_situation] #lisab laua voimalike laudade listi

                if 0 <= piece[0]-1 <= 7 and 0 <= piece[1]-1 <= 7:
                    if situation[piece[0]-1][piece[1]-1] == 0: #Kui on tuhi koht
                        temp_situation = deepcopy(situation)
                        temp_situation[piece[0]][piece[1]] = 0
                        temp_situation[piece[0]-1][piece[1]-1] = [piece[0]-1, piece[1]-1, 1]
                        future_boards += [temp_situation] #lisab laua voimalike laudade listi

                    if type(situation[piece[0]-1][piece[1]-1]) == list: #kui on nupp
                        if situation[piece[0]-1][piece[1]-1][2] == 0: #Kui on tais koht ja vastaskabend
                            if 0 <= piece[0]-2 <= 7 and 0 <= piece[1]-2 <= 7:
                                if situation[piece[0]-2][piece[1]-2] == 0: #Kui taga on tuhi
                                    temp_situation = deepcopy(situation)
                                    temp_situation[piece[0]][piece[1]] = 0
                                    temp_situation[piece[0]-1][piece[1]-1] = 0
                                    temp_situation[piece[0]-2][piece[1]-2] = [piece[0]-2, piece[1]-2, 1]
                                    future_boards += [temp_situation] #lisab laua voimalike laudade listi

    return  future_boards

def evaluation(laud):
    n_white = 0
    n_black = 0
    for col in range(8):
        for row in range(8):
            if type(laud[col][row]) == list:
                if laud[col][row][2] == 0:
                    n_white += 1
                if laud[col][row][2] == 1:
                    n_black += 1
    dif = n_white - n_black
    return dif

#TEST

#board = board_detection()[0]

#for tulp in board:
#    print(tulp)
#print(" ")

#lauad = possible_moves(board, "white")

#for ld in lauad:
#    for tulp in ld:
#        print(tulp)
#    print(" ") 