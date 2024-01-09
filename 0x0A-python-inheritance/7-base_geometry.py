#!/usr/bin/python3
"""
this module is define a class
"""


class BaseGeometry:
    """this class is conatain a public mothode
    that print a message exception that told
    a specific message
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this methode take two argument as
        a parameter that validate the input
        args:
            parameter1: name is a string
            parameter2: value is an integer
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
