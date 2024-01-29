#!/usr/bin/python3
""" an rectangle definition """


class Rectangle:
    """ An empty rectangle class """
    def __init__(self, width=0, height=0):
        """ initialiser for a rectangle
        Args:
            Width - width of the rectangle
            height - height of the rectangle
        Raises:
            typeError: if width or heigjt are not ints
            ValueError: if height or width are less than 0
            """
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
