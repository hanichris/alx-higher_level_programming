#!/usr/bin/python3
"""Module that defines class MyInt."""


class MyInt(int):
    """Extends int class."""

    def __eq__(self, other):
        """Redefine method to mean !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Redefine method to mean ==."""
        return super().__eq__(other)
