#!/usr/bin/python3

'''Task 3'''


import json


def to_json_string(my_obj):
    '''function that returns the JSON representation
    of an object (string)'''
    x = json.dumps(my_obj)
    return x
