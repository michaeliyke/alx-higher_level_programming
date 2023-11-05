#!/usr/bin/python3


def no_c(my_string):
    s = ""
    for x in my_string:
        if x not in "cC":
            s += x
    return s
