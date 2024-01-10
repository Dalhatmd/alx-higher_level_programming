#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = sorted(a_dictionary.keys())
    for key in sort:
        print(f"{key}: {a_dictionary[key]}")
