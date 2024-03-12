"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(3)

    def test_add_area(self):
        c1 = self.circle
        c2 = Circle(2)
        c3 = c1.add_area(c2)
        c3_radius = math.hypot(c1.get_radius(), c2.get_radius())
        self.assertEqual(c3_radius, c3.get_radius())
        self.assertEqual(c3.get_area(), math.pi*(c3_radius**2))

    def test_radius_is_zero(self):
        c1 = Circle(0)
        new_circle = self.circle.add_area(c1)
        c3 = c1.add_area(new_circle)
        self.assertEqual(c3.get_radius(), new_circle.get_radius())
        self.assertEqual(c3.get_area(), math.pi*(c3.get_radius()**2))

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            c1 = Circle(-1)
            c2 = Circle(-10)

