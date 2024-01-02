#!/usr/bin/python3
def remove_char_at(word, n):
    copy = str(word)
    try:
        copy = copy.replace(copy[n], '')
    except:
        return word
    return copy

#print(remove_char_at("Chicago", 16))
