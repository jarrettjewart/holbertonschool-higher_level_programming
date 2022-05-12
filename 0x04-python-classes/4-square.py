#!/usr/bin/python3
"it's a square class"


class Square:
    "square class with only a private size"
    def __init__(self, size=0):
        sefl.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size) == 0:
            print()
        else:
            for i in range(slef.__size):
                for i in range(self.__self):
                    print('#', end="")
                print()
