#!/usr/bin/python3
"""
this module conatin a function that
returns Json representation of obj
"""


def to_json_string(my_obj):
    """this function take one parameter as an argument
    Args:
	parameter1: my_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)
