#!/usr/bin/python3
""" an empty rectangle definition """


class Rectangle:
    """ An empty rectangle class """
    def __init__(self, width=0, height=0):
        """ initialiser for a rectangle """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter foe width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Finds the area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ finds the perimeter of tge rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
