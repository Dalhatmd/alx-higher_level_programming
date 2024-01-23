#!/usr/bin/python3
class Square:
    """ A class that defines a square
    """
    def __init__(self, size=0):
        """Initializer for the square class
        Args:
            size(int): size of the square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
