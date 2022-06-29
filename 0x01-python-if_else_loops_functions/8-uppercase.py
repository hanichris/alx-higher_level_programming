#!/usr/bin/env python3

def uppercase(str):
    if str is None or str == '':
        raise ValueError
    for char in str:
        if char >= 'a' and char <= 'z':
            delta = ord(char) - 97
            uppercase_char = 65 + delta
            print("{:c}".format(uppercase_char), end="")
        else:
            print("{:s}".format(char), end='')
    print()
