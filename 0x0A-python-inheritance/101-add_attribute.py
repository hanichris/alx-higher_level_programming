#!/usr/bin/python3
"""Module that defines add_attribute() function."""


def add_attribute(obj, att, value):
    """Adds an attribute to an object if possible.

    Args:
        obj (object): Object to add an attribute to.
        att (str): Name of the attribute to add.
        value (str): Value of the attribute.

    Raises:
        TypeError: If not able to add the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
