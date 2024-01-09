#!/usr/bin/python3
"""
this module contain a class
named Square that iherent from
the Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that iherent from a Rectangle class"""
    def __init__(self, size):
        """intialization of the size argument"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """this methode print the string representation
        of width and height"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
