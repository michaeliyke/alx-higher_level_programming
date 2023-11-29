#!/usr/bin/python3
"""Rectange module"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.val_size(width, "width")
        self.val_size(height, "height")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the value of __width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets thje value of __width"""
        self.val_size(width, "width")
        self.__width = width

    @property
    def height(self):
        """Returns the value of __height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets thje value of __height"""
        self.val_size(height, "height")
        self.__height = height

    def val_size(self, size, side="width"):
        """Validates the value of width/height to avoid data corruption"""
        if type(size) is not int:
            raise TypeError("{} must be an integer".format(side))
        if size < 0:
            raise ValueError("{} must be >= 0".format(side))

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
