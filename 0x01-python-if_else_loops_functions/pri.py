#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, -1):
    if 'a' <= chr(i) <= 'z':
        print("{}".format(chr(i)), end='')
        continue
    if 'A' <= chr(i - 1) <= 'Z':
        print("{}".format(chr(i - 1)), end='')
