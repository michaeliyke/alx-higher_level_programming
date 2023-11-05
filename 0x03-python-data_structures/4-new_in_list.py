#!/usr/bin /python3


def new_in_list(my_list, idx, element):
    if not my_list:
        return my_list
    cpy = [i for i in my_list]
    if not isinstance(idx, int):
        return cpy
    if idx < 0 or idx >= len(my_list):
        return cpy
    cpy[idx] = element
    return cpy
