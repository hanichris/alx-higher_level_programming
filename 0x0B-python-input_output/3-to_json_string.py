#!/usr/bin/python3
"""Module that defines the to_json_string() function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.

    Args:
        my_obj (object): An instance of the class object.

    Return:
        str: string representation of the object.
    """
    return json.dumps(my_obj)
