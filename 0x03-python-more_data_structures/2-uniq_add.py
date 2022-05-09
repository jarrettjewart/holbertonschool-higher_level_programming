#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    for x in set(my_list):
        i += x
        return i
