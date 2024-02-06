#!/usr/bin/python3
""" Module to write to a file """


def write_file(filename="", text=""):
    """ Writes to a file """
    with open(filename, "w") as file:
        data = file.write(text)
        return data
