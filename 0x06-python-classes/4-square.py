#!/usr/bin/python3


class Square:
    """
    Class Square details

    Attributes:
        size (int): private instance attribute
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

    @property
    def size(self):
        """
        Returns the value of __size private instance variable
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of __size instance private variable
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        The area of the square object
        """
        return self.__size * self.__size
