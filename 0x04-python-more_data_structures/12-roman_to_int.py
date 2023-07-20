#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    roman_list = list(roman_string)
    roman_list.reverse()
    total = 0
    for i in range(len(roman_list)):
        if i == 0:
            total += roman_dict[roman_list[i]]
        elif roman_dict[roman_list[i]] >= roman_dict[roman_list[i - 1]]:
            total += roman_dict[roman_list[i]]
        else:
            total -= roman_dict[roman_list[i]]
    return total
