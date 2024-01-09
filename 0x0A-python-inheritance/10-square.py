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
        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size
