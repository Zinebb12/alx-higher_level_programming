#!/usr/bin/python3
"""
module (Same class or inherit from)
this function return true or false
"""


def is_kind_of_class(obj, a_class):
    """this function evaluate if
    obj is an instance from a_class
    this function take two parameter as anrgument
    args:
        parameter1: an object
        parameter2: a class
    return:
        return true or false
    """
    if isinstance(obj, a_class):
        return True
    return False
