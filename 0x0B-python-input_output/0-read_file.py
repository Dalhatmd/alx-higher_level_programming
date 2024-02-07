#!/usr/bin/python3
""" Module to read a file """


def read_file(filename=""):
    """ Reads a file """
    with open(filename, "r") as file:
        data = file.read()
        print(data, end='')
