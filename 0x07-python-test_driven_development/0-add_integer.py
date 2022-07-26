#!/usr/bin/python3
"""Module that defines a function to add 2 integers."""


def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int/float): first argument.
        b (int/float): second argument.
    Returns:
        int: a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
