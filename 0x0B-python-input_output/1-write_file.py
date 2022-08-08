#!/usr/bin/python3
"""Module with write_file() function definition."""


def write_file(filename="", text=""):
    """Write a string to a text file and return the character count.

    Args:
        filename (str): name of the file.
        text (str): string to write to text file.

    Returns:
        int: number of characters written.
    """
    with open(filename, mode="w", encoding='utf-8') as a_file:
        return a_file.write(text)
