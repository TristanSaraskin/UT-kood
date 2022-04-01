from kabelaud import board_detection
from pathlib import Path
import os

directory_test = (r'C:\Users\karva\Documents\KOOL\UT\Katsed_objektituvastus\andmestik')
directory_result = (r'C:\Users\karva\Documents\KOOL\UT\Katsed_objektituvastus\tulemus')

files = Path(directory_test).glob('*')

for file in files:
    name = os.path.basename(file)
    board_detection(str(file), str(directory_result), name)