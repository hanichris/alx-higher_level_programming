#!/usr/bin/python3
"""Module holding the read_file() definition."""


def read_file(filename=""):
    """Read a text file and print out the content to stdout.

    Args:
        filename (str): name of the text file.
    """
    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
