#!/usr/bin/python3
"""Module that holds the print_sorted() definition."""


class MyList(list):
    """Extension of the List class."""

    def print_sorted(self):
        """Print out a list in ascending order."""
        print(sorted(self))
