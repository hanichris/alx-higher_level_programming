#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Determines the peak element in a list of unsorted integers.

    Args:
        list_of_integers (list): unsorted list of integers.
    Return:
        peak (int): peak element in the list.
    """
    if not isinstance(list_of_integers, list):
        return
    if len(list_of_integers) == 0:
        return None
    low = 0
    high = n = len(list_of_integers) - 1

    while low <= high:
        mid = low + (high - low)//2
        if (mid == 0 or
                (list_of_integers[mid] > list_of_integers[mid - 1])) and\
                (mid == n or
                 list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid < n and (list_of_integers[mid+1] > list_of_integers[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return list_of_integers[low - 1] or list_of_integers[high + 1]
