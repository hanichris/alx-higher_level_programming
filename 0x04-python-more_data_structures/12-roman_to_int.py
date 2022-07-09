#!/usr/bin/python

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    convert_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i, char in enumerate(roman_string):
        if char in convert_table:
            result += convert_table[char]
        else:
            return 0
        if i:
            if (char == 'X' or char == 'V') and roman_string[i - 1] == 'I':
                result -= 2
            elif (char == 'L' or char == 'C') and roman_string[i - 1] == 'X':
                result -= 20
            elif (char == 'D' or char == 'M') and roman_string[i - 1] == 'C':
                result -= 200
    return result
