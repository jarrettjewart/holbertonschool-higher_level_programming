#!/usr/bin/python3
"it's a square class"


class Square:
    "square class with only a private size"
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

            def __init__(self, size=0):
                self.__size = size

                def area(self):
                    return self.__size ** 2
