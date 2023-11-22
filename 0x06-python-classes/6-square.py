#!/usr/bin/python3
"""The Square module. This module introduces the Square class and family
"""


class Square:
    """
    The base Square type
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square type

        Args:
            size (int, optional): length of the sides. Defaults to 0.
            position (tuple, optional): Position. Defaults to (0, 0).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be a real number
            TypeError: position must be a tuple of 2 integers
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not self.valid_pos(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Retrievs the value of __size

        Returns:
            int: the value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for __size

        Args:
            value (int): the value of __size

        Raises:
            TypeError: size must be an integer
            ValueError: size must be a real number
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        The area of the square object
        """
        return self.__size * self.__size

    @property
    def position(self):
        """Retreives the value of __position instance private attribute

        Returns:
            tuple: returns __position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the instance position to value

        Args:
            value (tuple): the new instance position

        Raises:
            TypeError: a valid position must be a tuple of two integers
        """
        if not self.valid_pos(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square"""
        if self.size == 0:
            print()

        x, y = self.position if self.position else (0, 0)
        if self.size < 1:
            return
        for line in range(y):
            print()

        for ch in range(self.size):
            for space in range(x):
                print(" ", end="")
            for c in range(self.size):
                print("#", end="")
            print()

    def valid_pos(self, pos):
        """Verify if pos is a valid position

        Args:
            pos (tuple): a valid position must be a tuple

        Returns:
            bool: True if valid and False if not
        """
        if not isinstance(pos, tuple) or len(pos) == 2:
            return False
        if not isinstance(pos[0], int) or not isinstance(pos[1], int):
            return False
        if pos[0] < 0 or pos[1] < 0:
            return False
        return True
