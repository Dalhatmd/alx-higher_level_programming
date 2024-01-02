#!/usr/bin/python3
for i in range(10):
    for ii in range(10):
        if ii == 9 and i == 9:
            print("{a}{b}".format(a=i, b=ii))
            break
        print("{a}{b}".format(a=i, b=ii), end=', ')
