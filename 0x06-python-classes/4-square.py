#!/usr/bin/python3
# 4-square.py by Dalhatmd
"""Defines a square"""


class Square:
    """Square blueprint"""

    def __init__(self, size=0):
        """ initializer for the square
        Args: size - size of the square
        Raises:
            TypeError: if size is not int
            ValueError: if size is not positive or 0
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """ size getter to receive size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ size setter to set size
        Args: value - value to be set as size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Function to find area of a square
        Returns: The area of the square
        """
        return (self.__size * self.__size)
