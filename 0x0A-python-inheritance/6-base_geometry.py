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
