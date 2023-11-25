#!/usr/bin/python3
"""
The ``0-add_integer`` module
"""


def add_integer(a, b=98):
    """Adds two integers or floats together

    Args:
        a (int, float): first operand
        b (int, float, optional): Second operand. Defaults to 98.

        Returns:
            (int, float)
    """

    b_is_num = type(b) is float or type(b) is int
    a_is_num = type(a) is float or type(a) is int

    if not a_is_num:
        raise TypeError("a must be an integer")
    if not b_is_num:
        raise TypeError("b must be an integer")

    if b + 1 == b:
        raise OverflowError("b too large")
    if a + 1 == a:
        raise OverflowError("a too large")

    return int(a + b)
