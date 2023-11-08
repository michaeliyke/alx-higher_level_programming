#!/usr/bin/python3


def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not a_dictionary: return None
    keys = list(a_dictionary.keys())
    b_key = keys[0]
    biggest = a_dictionary.get(b_key)
    for key in a_dictionary:
        if a_dictionary.get(key) > biggest:
            biggest = a_dictionary.get(key)
            b_key = key
    return b_key
