#!/usr/bin/python3
"""Base module"""
import json


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    def to_json_string(list_dictionaries: list) -> str:
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
