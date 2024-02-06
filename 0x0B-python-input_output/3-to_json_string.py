#!/usr/bin/python3
""" Module to serialize a string """


def to_json_string(my_obj):
    """ Converts a json representation to string """
    import json
    json_string = json.dumps(my_obj)
    return json_string
