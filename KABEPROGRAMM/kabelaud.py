import cv2
import os
import numpy
from copy import deepcopy

def board_detection(image_path):
    detected_coordinates = []#Koordinaatide hulk
    
    window_name = f"Detected Objects in {image_path}"
    original_image = cv2.imread(image_path)

    image_grey = cv2.cvtColor(original_image, cv2.COLOR_RGB2GRAY)

    whitechecker_classifier = cv2.CascadeClassifier(r"") #kirjuta siia valge kabendi kaskaadklassifitseerija faili asukoht
    blackchecker_classifier = cv2.CascadeClassifier(r"") #kirjuta siia musta kabendi kaskaadklassifitseerija faili asukoht
    checkerboard_classifier = cv2.CascadeClassifier(r"") #kirjuta siia kabelaua kaskaadklassifitseerija faili asukoht

    detected_whitecheckers = whitechecker_classifier.detectMultiScale(image_grey, minSize=(50, 50))
    detected_blackcheckers = blackchecker_classifier.detectMultiScale(image_grey, minSize=(50, 50))
    detected_checkerboards = checkerboard_classifier.detectMultiScale(image_grey, minSize=(200, 200))

    if len(detected_whitecheckers) != 0:
        for (x, y, width, height) in detected_whitecheckers:
            cv2.rectangle(original_image, (x, y), (x + height, y + width), (255, 0, 0), 2)
            detected_coordinates += [[(2*x + height)/2,(2*y + width)/2, 0]] #leiab tuvastatud valgete kabendite keskpunktid ja lisab need listina koordinaatide listi
        
    if len(detected_blackcheckers) != 0:
        for (x, y, width, height) in detected_blackcheckers:
            cv2.rectangle(original_image, (x, y), (x + height, y + width), (0, 0, 255), 2)
            detected_coordinates += [[(2*x + height)/2,(2*y + width)/2, 1]] #leiab tuvastatud mustade kabendite keskpunktid ja lisab need listina koordinaatide listi
        
    if len(detected_checkerboards) != 0:
        for (x, y, width, height) in detected_checkerboards:
            cv2.rectangle(original_image, (x, y), (x + width, y + height), (0, 255, 0), 2)
            x0_board = x 
            x1_board = x + width
            y0_board = y
            y1_board = y + height

        #pildil x suureneb paremale ja y suureneb alla
        laius = x1_board - x0_board
        laiusuhik = laius/8

        a = [x0_board, x0_board + laiusuhik]
        b = [x0_board + laiusuhik, x0_board + 2*laiusuhik]
        c = [x0_board + 2*laiusuhik, x0_board + 3*laiusuhik]
        d = [x0_board + 3*laiusuhik, x0_board + 4*laiusuhik]
        e = [x0_board + 4*laiusuhik, x0_board + 5*laiusuhik]
        f = [x0_board + 5*laiusuhik, x0_board + 6*laiusuhik]
        g = [x0_board + 6*laiusuhik, x0_board + 7*laiusuhik]
        h = [x0_board + 7*laiusuhik, x1_board]

        korgus = y1_board - y0_board
        korgusuhik = korgus/8

        VIII = [y0_board, y0_board + korgusuhik]
        VII = [y0_board + korgusuhik, y0_board + 2*korgusuhik]
        VI = [y0_board + 2*korgusuhik, y0_board + 3*korgusuhik]
        V = [y0_board + 3*korgusuhik, y0_board + 4*korgusuhik]
        IV = [y0_board + 4*korgusuhik, y0_board + 5*korgusuhik]
        III = [y0_board + 5*korgusuhik, y0_board + 6*korgusuhik]
        II = [y0_board + 6*korgusuhik, y0_board + 7*korgusuhik]
        I = [y0_board + 7*korgusuhik, y1_board]

        #laua maatriks
        board = []
        for i in range(8):
            board += [[0,0,0,0,0,0,0,0]]

        pieces = deepcopy(detected_coordinates)

        for i in pieces:
            if i[0] >= a[0] and i[0] <= a[1]:
                i[0] = 0
            elif i[0] >= b[0] and i[0] <= b[1]:
                i[0] = 1
            elif i[0] >= c[0] and i[0] <= c[1]:
                i[0] = 2
            elif i[0] >= d[0] and i[0] <= d[1]:
                i[0] = 3
            elif i[0] >= e[0] and i[0] <= e[1]:
                i[0] = 4
            elif i[0] >= f[0] and i[0] <= f[1]:
                i[0] = 5
            elif i[0] >= g[0] and i[0] <= g[1]:
                i[0] = 6
            elif i[0] >= h[0] and i[0] <= h[1]:
                i[0] = 7

        for i in pieces:
            if i[1] >= I[0] and i[1] <= I[1]:
                i[1] = 0
            elif i[1] >= II[0] and i[1] <= II[1]:
                i[1] = 1
            elif i[1] >= III[0] and i[1] <= III[1]:
                i[1] = 2
            elif i[1] >= IV[0] and i[1] <= IV[1]:
                i[1] = 3
            elif i[1] >= V[0] and i[1] <= V[1]:
                i[1] = 4
            elif i[1] >= VI[0] and i[1] <= VI[1]:
                i[1] = 5
            elif i[1] >= VII[0] and i[1] <= VII[1]:
                i[1] = 6
            elif i[1] >= VIII[0] and i[1] <= VIII[1]:
                i[1] = 7

        for piece in pieces:
            board[piece[0]][piece[1]] = piece
    
    #Kui soovid kuvada tuvastatud nupud ja laua vaheaknas, eemalda järgmiste ridade eest "#" märgid.
    #cv2.namedWindow(window_name, cv2.WINDOW_KEEPRATIO)
    #cv2.imshow(window_name, original_image)
    #salvestus
    #cv2.imwrite(os.path.join(result_path, filename), original_image)
    #cv2.resizeWindow(window_name, (800, 800))
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    if len(detected_checkerboards) != 0:
        return board
