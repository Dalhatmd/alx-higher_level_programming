#!/usr/bin/python3
""" Module that writes attributes of an object to a json file"""


def class_to_json(obj):
    """ prints the attributes of obj to a json file """
    json_dict = {}

    for attr in dir(obj):
        if not attr.startswith("__") and not callable(getattr(obj, attr)):
            attr_value = getattr(obj, attr)
            if isinstance(attr_value, (list, bool, dict, str, int, bool)):
                json_dict[attr] = attr_value

    return json_dict
