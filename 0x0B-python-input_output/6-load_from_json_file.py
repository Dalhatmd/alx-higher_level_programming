#!/usr/bin/python3
""" Module to load fr a json file """


def load_from_json_file(filename):
    """ loads an object from a json file """
    import json
    with open(filename, "r") as file:
        json_data = file.read()

    obj = json.loads(json_data)
    return (obj)
