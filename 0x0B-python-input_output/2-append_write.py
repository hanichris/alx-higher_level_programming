#!/usr/bin/python3
"""Module containing the definition of append_write()."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file and return character count.

    Args:
        filename (str): name of file.
        text (str): string to append to the end of a file.

    Returns:
        int: count of characters appended to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        return a_file.write(text)
