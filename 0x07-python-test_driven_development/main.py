#!/usr/bin/python3
"""Main module"""

mul = __import__("100-matrix_mul").matrix_mul


def pm(m):
    for arr in m:
        for e in arr:
            print(e, end=" ")
        print()


m = [[2, 3, 1], [4, 1, 5], [6, 2, 3]]
m2 = [[5, 6, 2], [7, 8, 4]]
mc = [[33, 40, 20], [37, 52, 32], [50, 64, 32]
      ]

pm(mc)
pm(mul(m, m2))
