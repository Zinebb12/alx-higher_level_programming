#!/usr/bin/python3
"""
Module Mylist

this module Contains class MyList that
inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """inherits methode from
    the list class
    """
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
