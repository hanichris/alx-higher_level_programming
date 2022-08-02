#!/usr/bin/python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Empty class."""

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
