#!/usr/bin/python3
""" A module to save to json file """


def save_to_json_file(my_obj, filename):
    """ saves to json file """
    import json
    with open(filename, "w") as file:
        json_data = json.dumps(my_obj)
        bytes_read = file.write(json_data)
        return bytes_read
