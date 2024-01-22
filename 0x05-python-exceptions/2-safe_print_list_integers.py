#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in my_list:
        try:
            print("{:d}".format(i), end='')
            num += 1
        except (ValueError, IndexError):
            break
    print()
    return (num)
