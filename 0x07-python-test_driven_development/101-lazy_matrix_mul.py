#!/usr/bin/python3
"""Matrix multiplication with numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies two matrices with numpy

    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Returns:
        list: the resulting matrix
    """
    a = m_a
    b = m_b
    if type(a) is not list:
        raise TypeError("m_a must be a list")
    if type(b) is not list:
        raise TypeError("m_b must be a list")

    sze = len(a[0]) if len(a) > 0 and type(a[0]) is list else 0
    for lst in a:
        if type(lst) is not list:
            raise TypeError("m_a must be a list of lists")
        for e in lst:
            if type(e) not in (float, int):
                raise TypeError("m_a should contain only integers or floats")
        if len(lst) != sze:
            raise TypeError("each row of m_a must be of the same size")

    sze = len(b[0]) if len(b) > 0 and type(b[0]) is list else 0
    for lst in b:
        if type(lst) is not list:
            raise TypeError("m_b must be a list of lists")
        for e in lst:
            if type(e) not in (float, int):
                raise TypeError("m_b should contain only integers or floats")
        if len(lst) != sze:
            raise TypeError("each row of m_b must be of the same size")

    if len(a) == 0 or len(a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(b) == 0 or len(b[0]) == 0:
        raise ValueError("m_b can't be empty")
    if len(a[0]) != len(b):  # xm == my
        raise ValueError("m_a and m_b can't be multiplied")

    np_arr_a = np.array(a)
    np_arr_b = np.array(b)
    np_res = np_arr_a.dot(np_arr_b)
    return np_res.tolist()
