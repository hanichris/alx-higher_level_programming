#!/usr/bin/python3

"""Module that holds the definition of a Square class."""


class Square:
    """Models a square."""

    def __init__(self, size=0):
        """Initialize a square object.

        Args:
            size (int): The size of the square object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
