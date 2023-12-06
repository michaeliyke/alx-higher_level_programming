#!/usr/bin/python3
"""Student To JSON With filter module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instance of the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) in (list, tuple):
            d = {}
            for key in self.__dict__.keys():
                if key in attrs:
                    d[key] = self.__dict__[key]
            return d

        return self.__dict__
