#!/usr/bin/python3
"""Module to test the Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Test class Rectangle instantiation."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(12, 4), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_args(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_id_creation(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id + 1, r2.id)

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.id + 1, r2.id)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r1.id, r2.id - 1)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 12, 45)

    def test_unique_id_assignment(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_width_access(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__width)

    def test_height_access(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__height)

    def test_x_access(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__x)

    def test_y_access(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 2, 0, 0, 12).__y)

    def test_width_getter(self):
        self.assertEqual(Rectangle(5, 9, 1, 2, 7).width, 5)

    def test_height_getter(self):
        self.assertEqual(Rectangle(5, 9, 1, 2, 7).height, 9)

    def test_x_getter(self):
        self.assertEqual(Rectangle(5, 9, 1, 2, 7).x, 1)

    def test_y_getter(self):
        self.assertEqual(Rectangle(5, 9, 1, 2, 7).y, 2)

    def test_width_setter(self):
        r = Rectangle(5, 9, 1, 2, 7)
        r.width = 6
        self.assertEqual(r.width, 6)

    def test_height_setter(self):
        r = Rectangle(5, 9, 1, 2, 7)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_x_setter(self):
        r = Rectangle(5, 9, 1, 2, 7)
        r.x = 2
        self.assertEqual(r.x, 2)

    def test_y_setter(self):
        r = Rectangle(5, 9, 1, 2, 7)
        r.y = 3
        self.assertEqual(r.y, 3)
