#!/usr/bin/python3
"""Module that defines the Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangular object by extending BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangular object.

        Validates the width and height before assigning them to private
        variables. If width/height is <= 0 or not an `int` an error is
        raised.

        Args:
            width (int): Shorter side of the rectangle.
            height (int): Longer side of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangular instance."""
        return self.__width * self.__height

    def __str__(self):
        """Return an informal string representation of the object."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
