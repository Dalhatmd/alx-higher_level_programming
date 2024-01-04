#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    s = add(a, b)
    diff = sub(a, b)
    prod = mul(a, b)
    divv = div(a, b)

    print("{} + {} = {}".format(a, b, s))
    print("{} - {} = {}".format(a, b, diff))
    print("{} * {} = {}".format(a, b, prod))
    print("{} / {} = {}".format(a, b, divv))
