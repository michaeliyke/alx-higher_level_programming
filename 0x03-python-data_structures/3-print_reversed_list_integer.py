#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for i in range(len(my_list)):
        if isinstance(i, int):
            x = (i + 1) * -1
            print("{:d}".format(my_list[x]))
