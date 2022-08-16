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


class TestRectangle_width(unittest.TestCase):
    """Test the width argument of a rectangular object."""

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)

    def test_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.4, 2)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"1": 3}, 2)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2, 6, 9}, 2)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((3, 7, 0), 2)

    def test_width_boolean(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_acceptable_width(self):
        self.assertIsInstance(Rectangle(1, 2), Rectangle)


class TestRectangle_height(unittest.TestCase):
    """Test the width argument of a rectangular object."""

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")

    def test_height_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.4)

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"1": 3})

    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {2, 6, 9})

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (3, 7, 0))

    def test_height_boolean(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, True)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_acceptable_height(self):
        self.assertIsInstance(Rectangle(1, 2), Rectangle)


class TestRectangle_x(unittest.TestCase):
    """Test the x argument of a rectangular object."""

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")

    def test_x_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.4)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3])

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"1": 3})

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {2, 6, 9})

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (3, 7, 0))

    def test_x_boolean(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_acceptable_x(self):
        self.assertIsInstance(Rectangle(1, 2, 3), Rectangle)


class TestRectangle_y(unittest.TestCase):
    """Test the y argument of a rectangular object."""

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_y_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.4)

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, [1, 2, 3])

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {"1": 3})

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {2, 6, 9})

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, (3, 7, 0))

    def test_y_boolean(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -3)

    def test_acceptable_y(self):
        self.assertIsInstance(Rectangle(1, 2, 3, 4), Rectangle)
