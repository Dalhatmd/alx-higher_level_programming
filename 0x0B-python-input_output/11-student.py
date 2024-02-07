#!/usr/bin/python3
"""A student class module """


class Student:
    """ A student blueprint """
    def __init__(self, first_name, last_name, age):
        """initialiser for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a json representation of the object"""
        if attrs is None:
            return {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                    }
        else:
            return {
                    attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """ Reloads attribute values from a json file """
        for attr_name, attr_value in json.items:
            if hasattr(self, attr_name):
                setattr(self, attr_name, attr_value)
