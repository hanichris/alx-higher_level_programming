#!/usr/bin/python3

"""Module that holds the definition of a Square class."""


class Square:
    """Models a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object.

        Args:
            size (int): The size of the square object.
            position (tuple): The offset for the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Access the private attribute size.

        Perform checks on the object variable before
        assigning it to the private attribute size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the square area."""
        return self.size ** 2

    def my_print(self):
        """Print out the square instance using '#' character."""
        if self.size == 0:
            print()

        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(' ', end="")
                for j in range(self.size):
                    print('#', end="")
                print()
