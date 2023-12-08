#!/usr/bin/python3
"""Models Rectangle test module"""

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Rectangle Test class"""

    def test_getters_n_setters(self):
        """Test the getters and setters"""
        a = Rectangle(10, 2)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)

        a.width = 20
        a.height = 20
        a.x = 2
        a.y = 2
        self.assertEqual(a.width, 20)
        self.assertEqual(a.height, 20)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 2)
