#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (len(sentence), None)
    length, first = (len(sentence), sentence[0])

    return (length, first)
