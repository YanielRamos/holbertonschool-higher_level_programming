#!/usr/bin/python3

"""class Mylist"""


class MyList(list):
    def __init__(self):
        pass

    def print_sorted(self):
        """function that sort a list"""
        if isinstance(self, list):
            sortlist = sorted(self)
            print(sortlist)
