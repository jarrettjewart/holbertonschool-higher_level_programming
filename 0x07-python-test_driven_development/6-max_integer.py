#!/usr/bin/python3
"""
Mod to find max int
"""


def max_integer(list=[]):
    """
    Function to find and return max int 
    Return: none if list is empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
