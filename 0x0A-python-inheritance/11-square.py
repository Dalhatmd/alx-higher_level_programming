#!/usr/bin/python3
""" A module for a square subclass """
Rectangle = __import__("10-square").Rectangle


class Square(Rectangle):
    """ A square class inheriting from basegeometry"""
    def __init__(self, size):
        """initialiser for the square class """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def __repr__(self):
        return f"[Square] {self.__size}/{self.__size}"
