#!/usr/bin/python3
""" A base class module """


class Base:
    """A base class blueprint """
    __nb_objects = 0

    def __init__(self, id=None):
        """initializer for Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
