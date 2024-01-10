#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = {key: a_dictionary[key] for key in sorted(a_dictionary.keys())}
    print(sort)
    return sort
