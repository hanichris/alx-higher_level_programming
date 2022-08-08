#!/usr/bin/python3
"""Module defining save_to_json_file() function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation.

    Args:
        my_obj (object): object to be serialized into a file.
        filename (str): name of file to write to.
    """
    with open(filename, mode="w", encoding='utf-8') as a_file:
         json.dump(my_obj, a_file)
