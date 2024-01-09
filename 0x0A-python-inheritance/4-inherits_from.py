#!/usr/bin/python3
"""
module: (Only sub class of)
this module ratuen true or false
in case of succuss or failure
"""


def inherits_from(obj, a_class):
    """
    this function check if class inherent
    dirictly from the parent class or not
    this function take two argument as a
    parameter
    args:
        parameter1: object
        parameter2: a class
    return:
        return true or false
    """
    return (type(obj) != a_class and issubclass(type(obj), a_class))
