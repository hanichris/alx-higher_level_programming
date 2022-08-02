#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Parent class for base geometry definition."""

    def area(self):
        """Unimplemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str)
            value (int)

        Raises:
            TypeError if value is not an integer.
            ValueError if value is <= 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

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
