#!/usr/bin/python3
"""
a function that prints a square using #
python3 -c 'print(__import__("my_module").__doc__)'
"""


def print_square(size):
    """
    print_square - fuction that prints a square using #
    size: Size of square
    Return: Square with #
    python3 -c 'print(__import__("my_module").__doc__)'
    """
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for lines in range(0, size):
        for hashes in range(0, size):
            print("#", end="")
        print("")
