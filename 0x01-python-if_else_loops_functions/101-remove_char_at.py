#!/usr/bin/python3
def remove_char_at(word, n):
    copy = str(word)
    if (n < 0):
        return word
    try:
        copy = copy.replace(copy[n], '')
    except IndexError:
        return word
    return copy
