#!/usr/bin/python3
# 1-square.py by Dalhatmd
""" Defines a square class """


class Square:
    """ A class that instantiates a square with a private instamce size"""

    def __init__(self, size):
        """ Instantiation with size
        Args: size - size of the square
        """

        self.__size = size
