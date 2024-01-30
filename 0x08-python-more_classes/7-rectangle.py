#!/usr/bin/python3
""" a rectangle definition """


class Rectangle:
    """ An empty rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialiser for a rectangle """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ prints a string representation of the string """
        rect = ''
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(self.__height):
            rect += str(Rectangle.print_symbol) * self.width
            if i == self.__height - 1:
                continue
            rect += '\n'
        return rect

    def __repr__(self):
        """ returns a string representation to use eval to
        create a new rectangle """
        return f"Rectangle ({self.width}, {self.height})"

    def __del__(self):
        """ defines what to do when an instance is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
