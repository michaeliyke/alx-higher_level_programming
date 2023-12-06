#!/usr/bin/python3
"""Module that returns dictionary discription of an object"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
     for JSON serialization of an object"""
    if type(obj) in (dict, str, list, int, bool):
        return obj.__dict__
    elif isinstance(obj, object):
        return obj.__dict__
