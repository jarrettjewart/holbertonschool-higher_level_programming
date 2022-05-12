#!/usr/bin/python3
"it's a square class"


class Square:
    "square class with only a private size"
    def __init__(self, size=0):
        is isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return ((self.__size) ** 2)
