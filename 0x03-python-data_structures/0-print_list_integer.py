#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if not my_list:
        return
    for i in my_list:
        if isinstance(i, int):
            print("{x:d}".format(x=i)) # print as a number without converting
