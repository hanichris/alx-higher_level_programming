#!/usr/bin/python3
"""Module defining pascal_triangle() function."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n.

    Args:
        n (int): size of the triangle.

    Return:
        list(list): Representation of Pascal's triangle.
    """
    res = []
    if n <= 0:
        return res
    for row in range(1, n+1):
        coeff = 1
        temp = []
        for k in range(1, row + 1):
            temp.append(coeff)
            coeff = int(coeff * (row - k) / k)
        res.append(temp)
    return res
