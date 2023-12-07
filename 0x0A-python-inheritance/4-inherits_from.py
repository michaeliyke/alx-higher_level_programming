#!/usr/bin/python3
"""Inherits from module"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    return isinstance(obj, type) and issubclass(obj, a_class)
