#!/usr/bin/python3
""" Print
a
matrix
divide
"""


def matrix_divided(matrix, div):
    """ Divide
    a
    matriz """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(rw, list) for rw in matrix) or
        not all((isinstance(elem, int) or isinstance(elem, float)
                for elem in [n for rw in matrix for n in rw]))):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(rw) == len(matrix[0]) for rw in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if ((not isinstance(div, int) and not isinstance(div, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), i)) for i in matrix])
