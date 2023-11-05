#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    ret = []
    for e in my_list:
        ret.append(abs(e) % 2 == 0)
    return ret
