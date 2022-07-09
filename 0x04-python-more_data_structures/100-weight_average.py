#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    num = sum(elem[0] * elem[1] for elem in my_list)
    den = sum(elem[1] for elem in my_list)
    return num / den
