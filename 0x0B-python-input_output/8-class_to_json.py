#!/usr/bin/python3
"""Module containing class_to_json() function definition."""


def class_to_json(obj):
    """Return dictionary description for JSON serialization.

    Args:
        obj (object): Instance of a class.

    Returns:
        json (str): Serialization of dictionary description.
    """
    return obj.__dict__
