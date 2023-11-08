#!/usr/bin/python3


def array_sq(arr):
    cpy = []
    for i in arr:
        cpy.append(i*i)
    return cpy

def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix."""
    matrix2=[]
    for arr in matrix:
        matrix2.append(array_sq(arr=arr))
    return matrix2
