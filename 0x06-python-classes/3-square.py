#!/usr/bin/python3
"""The Square module. This module introduces the Square class and family
"""


class Square:
    """
    The base Square type
    """

    def __init__(self, size=0):
        """
        Instantiation work happens here

        Args:
            size (int): size of square sides
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        The area of the square object
        """
        return self.__size * self.__size
