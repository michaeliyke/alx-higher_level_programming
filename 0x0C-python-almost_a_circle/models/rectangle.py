#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        super().__init__(id=id)

        self.validate("width", width)
        self.validate("height", height)
        self.validate("x", x)
        self.validate("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.width * self.height

    def validate(self, name: str, value):
        """Integer validation for width, height, x, y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ("width", "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if name in ("x", "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        return True

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        self.validate("width", width)
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        self.validate("height", height)
        self.__height = height

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        self.validate("y", y)
        self.__y = y

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        self.validate("x", x)
        self.__x = x
