#!/usr/bin/python3
""" A mdoule that append texts to a file """


def append_after(filename="", search_string="", new_string=""):
    """ appends a file """
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_lines.append(line)
        if search_string in line:
            modified_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)
