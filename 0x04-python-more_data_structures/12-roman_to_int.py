#!/usr/bin/python3
def roman_to_int(roman_string):
    for i in range(len(roman_string)):
        num = 0
        if roman_string[i] == 'I' and roman_string[i + 1]:
            num += 1
        else:
            num -= 1
        if roman_string[i] == 'V':
            num += 5
        if roman_string[i] == 'X':
            num += 10
    return num

print(roman_to_int('XX'))
#print(roman_to_int('XI'))
print(roman_to_int('VV'))
#print(roman_to_int('VI'))
print(roman_to_int('X'))
print(roman_to_int('V'))
