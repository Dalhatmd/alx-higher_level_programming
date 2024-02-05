#!/usr/bin/python3
"""A basegeometry class """


class BaseGeometry:
    """ A badegeometry class"""
    def area(self):
        """ Raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value input """
        self.name = name
        self.value = value
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ A rectanglr class """
    def __init__(self, width, height):
        """Initialiser for rectangle class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
