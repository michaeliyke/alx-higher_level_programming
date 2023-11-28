#!/usr/bin/python3
"""Matrix multiplication module"""


def matrix_mul(m_a, m_b):
    """function that multiplies two matrices

    if a is `xm` and b is `my` then c will be `xy` - dimensions

    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Returns:
        list: the resulting matrix
    """
    a = m_a
    b = m_b
    c = []
    if type(a) is not list: raise TypeError("m_a must be a list")
    if type(b) is not list: raise TypeError("m_b must be a list")
    for l in a:
        if type(l) is not list: raise TypeError("m_a must be a list of lists")
        for e in l:
            if type(e) not in (float, int):
                raise TypeError("m_a should contain only integers or floats")
    for l in b:
        if type(l) is not list: raise TypeError("m_b must be a list of lists")
        for e in l:
            if type(e) not in (float, int):
                raise TypeError("m_b should contain only integers or floats")
        
    if len(a) == 0 or len(a[0]) == 0: raise ValueError("m_a can't be empty")
    if len(b) == 0 or len(b[0]) == 0: raise ValueError("m_b can't be empty")
    if len(a[0]) == len(b):  # xm == my
        for _ in range(len(a)):
            c.append([0 for _ in range(len(b[0]))])
    else:
        raise TypeError("each row of m_a must be of the same size")
    for i in range(len(a)):
        for k in range(len(c)):
            sum = 0
            for j in range(len(b)):
                sum += a[i][k] * b[k][j]
            c[i][j] = sum

    return c
