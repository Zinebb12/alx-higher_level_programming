#!/usr/bin/python3
"""class that create a rectangle"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """return the size of rectagle"""
        return self.__size

    @size.setter
    def size(self, value):
        """update the sizeof a rectangle"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of a rectangle"""
        return self.__size ** 2

    def my_print(self):
        """print a square using #"""
        for _ in range(self.size):
            print('#' * self.size)

        if not self.size:
            print()
