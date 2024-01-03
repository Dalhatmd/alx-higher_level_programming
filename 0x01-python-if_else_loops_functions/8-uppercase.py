#!/usr/bin/python3
def uppercase(word):
    result = ''
    for letter in word:
        asc = ord(letter)
        if 97 <= asc <= 122:
            asc -= 32
        result += chr(asc)
    return result
