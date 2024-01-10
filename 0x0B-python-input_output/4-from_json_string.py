#!/usr/bin/python3
"""
this module contain a function that
returns python data structure from JSON string
"""


def from_json_string(my_str):
    """this function take one parameter as an argumet
    Args:
        my_str: json string representation
    Return:
        python object
    """
    import json

    return json.loads(my_str)
