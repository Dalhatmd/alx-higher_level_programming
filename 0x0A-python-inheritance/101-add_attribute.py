#!/usr/bin/python3
""" A module that adds an attribute to an object if possible"""


def add_attribute(obj, attribute_name, attribute_value):
    """
    Adds a new attribute if possible
    Args:
        obj - input object
        attribute_name - name of the attribute
        attribute_value value of the attribute
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
