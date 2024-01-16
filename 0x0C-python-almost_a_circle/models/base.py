#!/usr/bin/python3
"""Module for base class"""


class Base:
    """
    Base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - initialization
        Args:
            id: object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
