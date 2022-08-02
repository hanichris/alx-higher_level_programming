#!/usr/bin/python3
"""Module that defines the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square object by extending Rectangle."""

    def __init__(self, size):
        """Initializes Square instance.

        Args:
            size (int): side length of the square.
        """
        if self.integer_validator("size", size) is None:
            super().__init__(size, size)
            self.__size = size

    def area(self):
        """Return the area of a square."""
        return self.__size ** 2
