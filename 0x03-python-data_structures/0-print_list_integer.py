#!/usr/bin/python3


def print_list_integer(my_list=[]):
    if not my_list:
        return
    for i in my_list:
        if type(i) == int:
            print("{0}".format(i))
