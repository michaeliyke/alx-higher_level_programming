#!/usr/bin /python3


def new_in_list(my_list, idx, element):
    my_list = my_list if my_list else []
    cp = []
    for i in range(len(my_list)):
        e = my_list[i] if i != idx else element
        cp[i] = e
