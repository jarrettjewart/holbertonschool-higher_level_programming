#!/usr/bin/python3
"it's a square class"


class Square:
    "square class with only a private size"
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raie ValueError("size must be >= 0")
            self.__size = size

            def area(self):
                return self.__size * self.__size

            @propert
            def size(self):
                return(self.__size)

            @size.setter
            def sie(self, value):
                if type(value) is not int:
                    raise TypeError("size must be an integer")
                if value < 0:
                    raise ValueError("size must be >= 0")
                self.__size = value
