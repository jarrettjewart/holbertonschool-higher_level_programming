#!/usr/bin/python3
"""
Function that divides elements of a matrix
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def matrix_divided(matrix, div):
    """
    Function that divides elements of a matrix
    matrix_divided - divides elemnts of matrix
    matrix: matrix to divide
    div: num divided by
    Return: new matrix
    python3 -c 'print(__import__("my_module").__doc__)
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        for el in row:
            if isinstance(el, (int, float)) is False:
                raise TypeError(err)
    length = len(row)
    for row in matrix:
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if isinstance(div, (int, float)) if False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for row in range(len(matrix)):
        new.append(list(map(lambda i: i / div, matrix[row])))
        new[row] = list(map(lambda r: round(r, 2), new[row]))
    return new
