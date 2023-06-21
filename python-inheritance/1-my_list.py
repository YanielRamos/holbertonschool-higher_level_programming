#!/usr/bin/python3

"""class Mylist"""


class MyList(list):
    """method that sort a list"""

    def print_sorted(self):
        if isinstance(self, list):
            sortlist = sorted(self)
            print(sortlist)
