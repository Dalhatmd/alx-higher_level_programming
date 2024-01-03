#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        a = 0
    else:
        a = 32
    print("{}".format(chr(i - a)), end='')
