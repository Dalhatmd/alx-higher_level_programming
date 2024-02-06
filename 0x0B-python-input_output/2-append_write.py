#!/usr/bin/python3
""" Module to append to a file """


def append_write(filename="", text=""):
    """ appends @text to @filename """
    with open(filename, "a") as file:
        data = file.write(text)
        return data
