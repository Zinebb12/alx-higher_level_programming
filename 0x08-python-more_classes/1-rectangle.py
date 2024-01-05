#!/usr/bin/python3
"""
Create a class Rectangle
"""


class Rectangle:
    """class that define a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization of a Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """return the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set a new value to the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set a new value to the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
