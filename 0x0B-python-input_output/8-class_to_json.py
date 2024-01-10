#!/usr/bin/python3
"""

this module contain a function
that return dictinary representation
of a file
"""


def class_to_json(obj):
    """Returns dictionary representation of
       an object
    Args:
        obj: python object
    """
    return obj.__dict__
