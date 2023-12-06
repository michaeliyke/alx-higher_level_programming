#!/usr/bin/python3
"""From JSON To Object module"""
import json


def from_json_string(my_str):
    """Returns a data structure represented by a JSON string"""
    obj_json = json.loads(my_str)
    return obj_json
