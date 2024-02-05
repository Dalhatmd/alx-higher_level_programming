#!/usr/bin/python3
""" module to find if an oblect is a member of a class """


def is_same_class(obj, a_class):
    """ returns true if obj is a member of a_class """

    return type(obj) == a_class
