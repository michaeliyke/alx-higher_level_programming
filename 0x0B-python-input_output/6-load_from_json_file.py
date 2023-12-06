#!/usr/bin/python3
"""Create object from json module"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file” """
    with open(filename, encoding="utf-8") as file_:
        data = json.loads(file_.read())
    return data
