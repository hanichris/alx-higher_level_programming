#!/usr/bin/python3
"""Module with the definition of class Base."""


class Base:
    """Serves as the base class of all the other classes.

    Manages the `id` attribute of all future classes avoiding
    code duplication.

    Attributes:
        __nb_objects (int): private class attribute to keep track
        of the number of objects generated.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a new Base object.

        Args:
            id (int): The unique identifier of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

