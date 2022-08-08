#!/usr/bin/python3
"""Module defining from_json_string() function."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string.

    Args:
        my_str (str): string to deserialize into an object.

    Return:
        object: The object that the JSON string represented.
    """
    return json.loads(my_str)
