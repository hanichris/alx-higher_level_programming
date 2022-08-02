#!/usr/bin/python3
"""Module that holds the inherits_from() definition."""


def inherits_from(obj, a_class):
    """Checks the membership of an object to a subclass.

    Args:
        obj (object): An instance of a class.
        a_class (class): A particular type.

    Returns:
        bool: True if obj inherited from type a_class. Otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
