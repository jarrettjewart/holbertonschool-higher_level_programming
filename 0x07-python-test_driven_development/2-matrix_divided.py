#!/usr/bin/python3
"""
matrix_divided:
    Divaides variables of matrix
"""


list_error = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """
    Checks if matrix is a list
    """
    if type(matrix) is not list:
        raise TypeError(list_error)
    size = len(matrix[0])
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) not in (int, float
                    raise TypeError(list_error)
    if type(div) not in (int, float):
    raise TypeError("div must be a number")
    if div == 0:
    raise ZeroDivsionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]
