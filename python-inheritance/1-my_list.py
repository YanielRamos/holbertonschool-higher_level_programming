#!/usr/bin/python3

"""class Mylist"""


class MyList(list):
    """init method"""

    def __init__(self):
        pass

    def print_sorted(self):
        """method that sort a list"""
        if isinstance(self, list):
            sortlist = sorted(self)
            print(sortlist)
