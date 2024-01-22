#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ret_list = []
    num = 0
    for i in range(list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            num = 0
        except ZeroDivisionError:
            print("division by zero")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            ret_list.append(num)
    return (ret_list)
