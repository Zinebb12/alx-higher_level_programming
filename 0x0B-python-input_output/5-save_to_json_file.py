#!/usr/bin/python3
"""
this module comtain a function that
writes Python obj to file using Json represenation
"""


def save_to_json_file(my_obj, filename):
    """this function contain two argument as a parameter
    Args:
        parameter1: my_obj: python object
        parameter2: file
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
