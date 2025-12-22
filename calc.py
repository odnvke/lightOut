import numpy as np

from config import chenge_self, sosedstvo, size_x, size_y, mode

mode_1 = np.array(
    [0, 1, 0,
     1, 2, 1,
     0, 1, 0])

mode_2 = np.array(
    [1, 0, 1,
     0, 2, 0,
     1, 0, 1])

matrix2 = np.zeros((size_x, size_y))
pmatrix = np.zeros((size_x, size_y))


def process_matrix_with_rule(matrix:np.ndarray, x:int, y:int, mode=0, chenge_self=True):
    global size_x, size_y

    matrix_mode = np.zeros((9))
    if mode == 0:
        matrix_mode = mode_1
    elif mode == 1:
        matrix_mode = mode_2
    elif mode == 2:
        matrix_mode[:] = 1

    for i in range(0, 9):
        if matrix_mode[i] == 0:
            continue
        if matrix_mode[i] == 1:
            _x = x+(i//3)-1
            _y = y+(i%3)-1

            if _x == 0: _x = size_x-1
            elif _x == size_x: _x = 0

            if _y == 0: _y = size_y-1
            elif _y == size_y: _y = 0

            if matrix[_x, _y] == 0:
                matrix[_x, _y] = 1
            else:
                matrix[_x, _y] = 0

        elif chenge_self and matrix[x, y] == 1:
            matrix[x, y] = 0
        elif chenge_self:
            matrix[x, y] = 1
    return matrix

def calc(matrix: np.ndarray) -> (np.ndarray, int):
    global matrix2, pmatrix

    if mode == 0:
        if np.all(matrix2 == 0):
            # если цель и текущая матраца пустая возврощяем 0 
            if not np.any(matrix):
                return 0

            matrix2 = matrix.copy()

        x, y = np.where(matrix2==1)
        x, y = x[0], y[0]
        matrix2[x, y] = 0

        matrix = process_matrix_with_rule(matrix, x, y, sosedstvo, chenge_self)


    if np.array_equal(matrix, pmatrix):
        return 1

    pmatrix = matrix.copy
    return matrix