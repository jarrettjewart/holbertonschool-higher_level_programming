#!/usr/bin/python3
"""
add_integer:
    Returns sum of two ints
"""


def add_integer(a b=98):
    """
    Change floats to ints
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int)a)
        if type(a) is not int:
            raise TypeError("a must be an integer")
        if type(b) is not int:
            raise TypeError("b must be an integer")
        return a + b
