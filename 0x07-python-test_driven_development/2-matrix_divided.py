#!/usr/bin/
"""
Write a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers amd floats
        div (int, float): a number > 0
    Returns:
        list
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:  # matrix must be a list itself
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    m = []
    for l in matrix:
        if type(l) is not list:  # matrix must contain lists only
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if len(l) != len(matrix[0]):  # matrix elements must be equal in size
            raise TypeError("Each row of the matrix must have the same size")

        lx = []  # start a new list
        for e in l:  # Only int and float allowed
            if type(e) is not int and type(e) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")
            lx.append(round(e / div, 2))  # Divide e by div and round to 2 dp
        m.append(lx)  # add new list to the new matrix

    return m
