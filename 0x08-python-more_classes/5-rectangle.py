#!/usr/bin/python3

"""Module that holds the definition of a Rectangle class."""


class Rectangle:
    """Models a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a rectangular object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the private attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the private attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the rectangle using the A=LW formula."""
        return self.width * self.height

    def perimeter(self):
        """Compute the perimeter of the rectangle using P=2(L+W)."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return printable representation of a rectangular object.

        Uses the '#' character to represent the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        for row in range(self.height):
            for col in range(self.width):
                print('#', end="")
            if row != self.height - 1:
                print()
        return ""

    def __repr__(self):
        """Return the string representation of a rectangular object.

        This allows for the recreation of a new instance using the
        eval() function.
        """
        rect = f"Rectangle({str(self.width)}, {str(self.height)})"
        return rect

    def __del__(self):
        """Print a message during an instance's deletion."""
        print("Bye rectangle...")
