#!/usr/bin/python3
""" 
Task 1
"""


class MyList(list):
    """ Class that extends `list` """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ Print list in ascending order """
        print(sorted(self))
