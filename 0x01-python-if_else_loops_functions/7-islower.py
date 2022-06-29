#!/usr/bin/python3

def islower(c):
    if c is None or c == '':
        raise ValueError
    if c >= 'a' and c <= 'z':
        return True
    return False
