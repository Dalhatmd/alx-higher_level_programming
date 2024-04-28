#!/usr/bin/python3
""" A mdoule that append texts to a file """


def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'a+') as file:
        for i in file:
            if i == search_string:
                text = file.write(search_string)
        return text
