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
    if matrix is None:
       raise TypeError(
               "matrix must be a matrix (list of lists)"
               " of integers/floats"
               )
    new_matrix = [row[:] for row in matrix]
    for row in new_matrix:
        if len(row) != len(new_matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for index, elem in enumerate(row):
            if type(elem) not in (int, float):
                raise TypeError(
                        "matrix must be a matrix (list of lists)"
                        " of integers/floats"
                        )
            row[index] = round(elem/div, 2)
    return new_matrix
