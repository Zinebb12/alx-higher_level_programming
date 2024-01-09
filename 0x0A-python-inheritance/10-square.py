#!/usr/bin/python3
"""
defines a new class square a sub class of rectangle
"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """class Square that iherent from a Rectangle class"""
    def __init__(self, size):
        """intialization of the size argument"""
        self.integer_validation("size", size)
        super().__init__(size, size)
        self.__size = size
