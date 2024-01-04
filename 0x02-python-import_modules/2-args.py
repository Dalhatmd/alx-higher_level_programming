#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    args = sys.argv
    i = 1
    if num == 1:
        print("{} arguments.".format(0))
    elif num == 2:
        print("{} argument.".format(num - 1))
    elif num > 2:
        print("{} arguments:".format(num - 1))
    for arg in args[1:]:
        print("{}: {}".format(i, arg))
        i += 1
