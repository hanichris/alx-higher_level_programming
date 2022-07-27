#!/usr/bin/python3
"""Function that divides all the elements of a matrix."""


def matrix_divided(matrix, div):
    """Divided the elements of matrix by div.

    Args:
        matrix ([[]]) : A list of list of ints or floats.
        div (int/float) : Divides the elements of matrix.
    Return:
        [[]]: A new matrix with the elements divided by div.
    """
    if type(div) not in (float, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or matrix is None
        or not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
        raise TypeError(
           "matrix must be a matrix (list of lists)"
           " of integers/floats"
           )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x/div, 2), row)) for row in matrix]
