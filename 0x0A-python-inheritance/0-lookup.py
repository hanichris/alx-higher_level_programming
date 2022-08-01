#!/usr/bin/python3
"""Module to that holds the lookup(obj) definition."""

def lookup(obj):
    """Return list of available attributes and methods.

    Args:
        obj (object): object to investigate.

    Returns:
        list: holds the attributes and methods of interest.
    """
    return dir(obj)
