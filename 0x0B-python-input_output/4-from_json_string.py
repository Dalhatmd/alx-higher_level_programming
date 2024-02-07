#!/usr/bin/python3
""" module to deserialize a json file """


def from_json_string(my_str):
    """ gets a string from json file """
    import json
    data_string = json.loads(my_str)
    return data_string
