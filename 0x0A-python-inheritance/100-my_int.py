#!/usr/bin/python3
""" A module defining my integer class """


class MyInt(int):
    """ A class inheriting from int"""
    def __eq__(self, other):
        if isinstance(other, int):
            return not super().__eq__(other)

    def __ne__(self, other):
        if isinstance(other, int):
            return not super().__ne__(other)
