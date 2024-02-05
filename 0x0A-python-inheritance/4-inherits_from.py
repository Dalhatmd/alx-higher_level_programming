#!/usr/bin/python3
""" Checks whether a variable inherits from a class """


def inherits_from(obj, a_class):
    """ returns true if obj inherits from a_class """
    return issubclass(type(obj), a_class)
