#!/usr/bin/python3
"""Save to json file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file_:
        num_written = file_.write(json.dumps(my_obj))
    return num_written
