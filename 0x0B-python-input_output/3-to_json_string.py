#!/usr/bin/python3
"""To JSON module"""
import json


def to_json_string(my_obj):
    """Returns the json representation of an object"""
    obj_json = json.dumps(my_obj)
    return obj_json
