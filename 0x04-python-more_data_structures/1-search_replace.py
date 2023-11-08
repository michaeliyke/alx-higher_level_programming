#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list."""
    new = []
    for i in my_list:
        if i == search:
            new.append(replace)
        else:
            new.append(i)
    return new
