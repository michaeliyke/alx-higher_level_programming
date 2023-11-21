#!/usr/bin/python3
"""The Square module. This module introduces the Square class and family
"""


class Square:
    """
    The base Square type
    """

    def __init__(self, size=0):
        """instantiation

        Args:
            size (int, optional): size of the sides. Defaults to 0.

        Raises:
            TypeError: must be integer
            ValueError: must be real number
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns the value of __size private instance variable

        Returns:
            int: the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of __size instance private variable

        Args:
            value (int): size int

        Raises:
            TypeError: must be integer
            ValueError: must be a real number
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square object

        Returns:
            int: the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """Class print press
        """
        if self.size == 0:
            print()
        for ch in range(self.size):
            for c in range(self.size):
                print("#", end="")
            print()
