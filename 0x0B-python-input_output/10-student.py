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
