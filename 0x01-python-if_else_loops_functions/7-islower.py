#!/usr/bin/python3
def islower(c):
    answer = ord(c)
    if answer in (97, 127):
        return True
    else:
        return False
