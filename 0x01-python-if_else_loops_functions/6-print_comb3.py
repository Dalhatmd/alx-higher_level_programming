#!/usr/bin/python3
for i in range(0, 9):
    for ii in range(i + 1, 10):
        print("{:d}{:d}".format(i, ii), end='')
        if i == 8 and ii == 9:
            print()
            break
        else:
            print(', ', end='')
