#!/usr/bin/python3
"""
this module contain a function that
writes to text file and returns num chars written
"""


def write_file(filename="", text=""):
    """function take two parameter as an argument"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
