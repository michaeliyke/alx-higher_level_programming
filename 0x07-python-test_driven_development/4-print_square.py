#!/usr/bin/python3
"""Write a function that prints a square with the character #"""


def print_square(size):
    """function that prints a square with the character #

    Args:
        size (int): the size length of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#"*size)
