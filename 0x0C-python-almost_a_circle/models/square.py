#!/usr/bin/python
"""The square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The sqaure class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The square constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square object"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Getting the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """Setting the size of the square"""
        self.validate("width", size)
        self.width = size
        self.height = size
