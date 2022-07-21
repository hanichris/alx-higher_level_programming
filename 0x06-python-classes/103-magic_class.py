#!/usr/bin/python3

"""Module that holds the definition of a Magic class."""

import math



class MagicClass:
    """Models a square."""

    def __init__(self, radius=0):
        """Initialize a new instance of MagiClass.

        Args:
            radius (int/float): radius of a circle.
        """
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the area of the MagicClass."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * math.pi * self.__radius
