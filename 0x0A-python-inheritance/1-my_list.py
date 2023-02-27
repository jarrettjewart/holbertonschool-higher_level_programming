#!/usr/bin/python3

'''Task 1'''


class MyList(list):
    '''class MyList'''
    def print_sorted(self):
        '''Function that prints the list,
        but sorted (ascending sort)'''
        print(sorted(self))
