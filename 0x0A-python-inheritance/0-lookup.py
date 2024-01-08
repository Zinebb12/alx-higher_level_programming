#!/usr/bin/python3

"""
This function represents an object attribute lookup method.
"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
