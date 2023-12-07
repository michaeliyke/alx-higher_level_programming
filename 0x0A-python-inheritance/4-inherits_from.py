#!/usr/bin/python3
"""Inherits from module"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    if type(obj) is a_class:
        return False
    return issubclass(obj.__class__, a_class)
