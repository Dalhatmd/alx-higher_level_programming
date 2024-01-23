#!/usr/bin/python3
# 5-square.py by Dalhatmd
"""Defines a square"""


class Square:
    """Square blueprint"""

    def __init__(self, size=0, position=(0, 0)):
        """ initializer for the square
            Args: size - size of the square
            Raises:
                TypeError: if size is not int
                ValueError: if size is not positive or 0
            """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        """returns area of a square"""
        return (self.__size * self.__size)

    @property
    def position(self):
        """ returns input position of a square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter method
        Args: value - a tuple of 2 positive integers
        Raises: TypeError if value is not a tuple or any element
        in tuple is not  an integer > 0
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ prints a square with position """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
