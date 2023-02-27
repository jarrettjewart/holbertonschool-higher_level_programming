#!/usr/bin/python3

'''Task 4'''


import json


def from_json_string(my_str):
    '''function that returns an object (Python data structure)
    represented by a JSON string'''
    s = json.loads(my_str)
    return s
