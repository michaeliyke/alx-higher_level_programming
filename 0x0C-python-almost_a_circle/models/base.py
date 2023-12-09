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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file_:
            if not list_objs:
                file_.write("[]")
            else:
                file_.write(Base.to_json_string(list_objs))

    @staticmethod
    def to_json_string(list_dictionaries: list) -> str:
        """returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps([
            rect.to_dictionary() if isinstance(rect, Base) else rect
            for rect in list_dictionaries
        ])
