#!/usr/bin/python3
""" program that adds 2 integers """


def add_integer(a, b=98):
    """ adds 2 integers
    Args:
        a - first integer
        b - second integer
    Raises: Value Error if argument is not an integer
    Returns: a + b
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise ValueError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise ValueError("b must be an integer")

    return int(a) + int(b)
