#!/usr/bin/python3
"""Module that holds the is_same_class() definition."""


def is_same_class(obj, a_class):
    """Checks the membership of an object to a class.

    Args:
        obj (object): An instance of a class.
        a_class (class): A particular type.

    Returns:
        bool: True if obj is of type a_class. Otherwise, False.
    """
    return type(obj) == a_class
