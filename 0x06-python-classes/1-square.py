#!/usr/bin/python3
class Square:
    """ A class that instantiates a square with a private instamce size
    """
    def __init__(self, size):
        """ Instantiation with size 
        Args:
            size(int): size of the square
        """
        self.__size = size
