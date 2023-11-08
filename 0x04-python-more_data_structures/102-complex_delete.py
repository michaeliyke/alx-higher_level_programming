#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary"""
    if not a_dictionary:
        return a_dictionary
    deleted = []
    for k in a_dictionary:
        if a_dictionary.get(k) == value:
            deleted.append(k)
    for d in deleted:
        del a_dictionary[d]
    return a_dictionary
