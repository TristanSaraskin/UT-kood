from kabelaud import board_detection
from minimax import minimax
from pathlib import Path
import os

def main():
    picture_directory = (r'C:\Users\karva\Documents\KOOL\UT\pildid ja kaskaadid\test')
    files = Path(picture_directory).glob('*')
    for file in files:
        detection_file = str(file)

    board = board_detection(detection_file)
    new_board = minimax(board, 4, True)[1]

    for col in range(8):
        for row in range(8):
            if board[col][row] != new_board[col][row]:
                if board[col][row] != 0:
                    first_pos = board[col][row]
                if new_board[col][row] != 0:
                    second_pos = new_board[col][row]

    x1 = first_pos[0]
    y1 = first_pos[1]
    x2 = second_pos[0]
    y2 = second_pos[1]

    return x1, y1, x2, y2
