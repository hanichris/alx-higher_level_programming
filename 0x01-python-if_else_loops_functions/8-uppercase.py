#!/usr/bin/python3

def uppercase(str):
    new_str = ''
    for char in str:
        if char >= 'a' and char <= 'z':
            delta = ord(char) - 97
            uppercase_char = 65 + delta
            new_str += chr(uppercase_char)
        else:
            new_str += char
    print("{:s}".format(new_str))
