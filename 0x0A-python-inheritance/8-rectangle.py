#!/usr/bin/python3

'''Task 8'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle'''

    def __init__(self, width, height):
        '''Initializing atributes'''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
