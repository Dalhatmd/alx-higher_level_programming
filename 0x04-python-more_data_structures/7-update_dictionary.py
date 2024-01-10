#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    try:
        a_dictionary[key] = value
        print(a_dictionary)
        return a_dictionary
    except KeyError:
        return None
