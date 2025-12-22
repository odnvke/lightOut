import sys
import os

import numpy as np
import time

from config import size_x, size_y
from calc import calc
from console import process_output, print_start, print_matrix

matrix:np.ndarray = np.zeros((size_x, size_y))
matrix[1, 1] = 1
matrix[2, 2] = 1
matrix[2, 4] = 1

step:int = 0

#    ####  START  PROGRAMM  ####
RUN = True
print_start()
print_matrix(matrix, step)
while RUN:
    print("\n\n\n\n\n")
    output = calc(matrix)
    RUN = process_output(output)
    if not RUN:
        break
    
    matrix = output
    print_matrix(matrix, step)

    step += 1
    time.sleep(0.0001)