#!/usr/bin/python3
"it's a square class"


class Square:
    "aquare class with only a private size"
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return self.__size * self.__size

        @property
        def
        size(self):
            return(self.__size)

        @size.setter
        def size(self, value):
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def my_print(self):
                if self.size > 0:
                    for i in range(self.__size):
                        for j in rage(self.__sie):
                            print("#", end="")
                        print()
                else:
                    print()
