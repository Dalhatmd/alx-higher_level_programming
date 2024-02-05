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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """ A square class inheriting from basegeometry"""
    def __init__(self, size):
        """initialiser for the square class """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
