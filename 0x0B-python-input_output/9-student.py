#!/usr/bin/python3
"""A module that defines a student class """


def class_to_json(obj):
    """ prints the attributes of obj to a json file """
    json_dict = {}
    for attr in dir(obj):
        if not attr.startswith("__") and not callable(getattr(obj, attr)):
            attr_value = getattr(obj, attr)
            if isinstance(attr_value, (list, bool, dict, str, int, bool)):
                json_dict[attr] = attr_value
    return json_dict


class Student:
    """ A student blueprint """
    def __init__(self, first_name, last_name, age):
        """initialiser for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a json representation of the object"""
        return class_to_json(self)
