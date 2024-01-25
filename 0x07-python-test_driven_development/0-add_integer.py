#!/usr/bin/python3
def add_integer(a, b=98):
    if not (isinstance(a, int) or not isinstance(b, int)):
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise ValueError("Both inputs must be integers")
    return (a + b)

import doctest
doctest.testfile("0-add_integer.txt")
