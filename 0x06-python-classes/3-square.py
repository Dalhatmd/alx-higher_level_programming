#!/usr/bin/python3
# 3-square.py by Dalhatmd
""" A square definition """


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """initialize square class
        Args: size - represents the size of a square
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """finds the area of the square"""

        return self.__size * self.__size
