#!/usr/bin/python3
"""Module with class Student definition."""


class Student:
    """Models a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student object.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve the dictionary representation of a Student instance.

        Args:
            attrs (list/None): list of attributes to retrieve. If None,
            retrieve all the attributes.
        """
        if type(attrs) is list:
            res = dict(filter(lambda x: x[0] in attrs,
                              self.__dict__.items()))
            return res
        return self.__dict__
