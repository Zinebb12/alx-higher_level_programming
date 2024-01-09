#!/usr/bin/python3
"""defines class rectangle that inherits from basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents rectangle class from basegeometry"""

    def __init__(self, width, height):
        """initializes new rectangle.

        Args:
            width (int): width of new rectengle
            height (int): height of new rectangle
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
