#!/usr/bin/python3
"""Module holding the tests for class Base."""
import unittest

from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """Tests different instantiations of class Base."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_with_arg(self):
        self.assertEqual(Base(12).id, 12)

    def test_post_arg(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b2.id + 1, b4.id)

    def test_access_private_attribute(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)
