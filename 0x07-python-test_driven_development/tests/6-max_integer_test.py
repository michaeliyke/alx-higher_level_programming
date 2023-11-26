#!/usr/bin/python3

"""
Max integer - Unittest
"""
from unittest import TestCase

maxint = __import__("6-max_integer").max_integer


class MaxIntegerTest(TestCase):
    """
    Max integer - Unittest
    """

    def test_max_integer(self):
        """
        unittests for the ``max_integer`` function
        """
        # Basic functionality
        self.assertEqual(maxint([1, 2, 3, 4, 5]), 5)
        self.assertEqual(maxint([-10, -8, -6, -4, -2]), -2)
        self.assertEqual(maxint([1, 2, -10, -8, 3, -6, -4, 5, -2]), 5)
        self.assertEqual(maxint([1, 2, -10, -8, 3, -6, -4, 0, -2]), 3)
        self.assertEqual(maxint([-7]), -7)

        # Edge cases
        self.assertEqual(maxint([]), None)
        self.assertEqual(maxint(list(range(0, 50100, 100))), 50000)

        # Special cases
        self.assertEqual(maxint([1, 2, 3, 4, 5, 3, 2, 8, 1, 5]), 8)
        self.assertEqual(maxint([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]), 5)
        self.assertEqual(maxint([5, 5, 5.65, 5, 5, 5, 6, 5]), 6)
