#!/usr/bin/python3
"""Models Base test module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """The TestBase class"""

    def test_instance_creation(self):
        """Testing the initilization of Base class"""
        a = Base(id=36)
        self.assertIsInstance(a, Base)
        self.assertEqual(a.id, 36)

        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)
