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

    def to_dictionary(self):
        """Converts the square object to a dictionary"""
        return {
            "x": self.x,
            "y": self.y,
            "size": self.size,
            "id": self.id,
        }

    def update(self, *args, **kwargs):
        """Updates a square object with new values"""
        if not args:
            props = ("id", "size", "x", "y")
            for key, value in kwargs.items():
                if key in props:
                    setattr(self, key, value)
            return

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

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
