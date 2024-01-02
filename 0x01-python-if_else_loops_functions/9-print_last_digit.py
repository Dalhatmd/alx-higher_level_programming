#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    result = number % 10
    print(result)

"""print(print_last_digit(98))
print(print_last_digit(0))
print(print_last_digit(-1088))"""
