#!/usr/bin/python3
def remove_char_at(word, n):
    copy = str(word)
    copy = copy.replace(copy[n], '')
    return copy
