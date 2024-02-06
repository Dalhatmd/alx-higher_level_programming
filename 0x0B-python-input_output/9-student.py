#!/usr/bin/python3
"""A module that defines a student class """


class_to_json = __import__('8-class_to_json').class_to_json


class Student:
    """ A student blueprint """
    def __init__(self, first_name, last_name, age):
        """initialiser for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return class_to_json(self)
