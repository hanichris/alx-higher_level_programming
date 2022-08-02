#!/usr/bin/python3
"""Module that holds the is_kind_of_class() definition."""


def is_kind_of_class(obj, a_class):
    """Checks the membership of an object to a class.

    Args:
        obj (object): An instance of a class.
        a_class (class): A particular type.

    Returns:
        bool: True if obj is of type a_class. Otherwise, False.
    """
    return isinstance(obj, a_class)
