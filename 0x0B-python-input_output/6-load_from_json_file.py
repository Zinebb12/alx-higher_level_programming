#!/usr/bin/python3
"""
this module contain a function that
creates a Python obj from Json file
"""


def load_from_json_file(filename):
    """function that take one argument as parameter
    Args:
        parameter1: filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
