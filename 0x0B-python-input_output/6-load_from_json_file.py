#!/usr/bin/python3
"""Module defining load_from_json_file() function."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): name of .json file.
    """
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
