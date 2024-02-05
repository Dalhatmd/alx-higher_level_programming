#!/usr/bin/python3
"""A basegeometry class """


class BaseGeometry:
    """ A badegeometry class"""

    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validatea the value input """
        self.name = name
        self.value = value

        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
