#!/usr/bin/python3
"""
this module contain a function that
writes to text file and returns num chars written
"""


def append_write(filename="", text=""):
    """function take two parameter as an argument"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
