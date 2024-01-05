#!/usr/bin/python3
def no_c(my_string):
    new = ""
    chars = ('c', 'C')
    for i in my_string:
        if i not in chars:
            new += i
    return new
