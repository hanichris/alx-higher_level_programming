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
        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height = height
