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

    def area(self):
        """return the area of a Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """claculate the priemeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        lenght_max = max(self.__height, self.__width)
        p = (lenght_max + self.__width) * 2
        return p

    def __str__(self):
        """ Prints rectangle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pic

    def __repr__(self):
        "return a string representation of an object"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
