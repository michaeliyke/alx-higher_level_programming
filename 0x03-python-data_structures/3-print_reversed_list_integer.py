#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        x = (i + 1) * -1
        print("{}".format(my_list[x]))
