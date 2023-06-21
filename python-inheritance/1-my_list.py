#!/usr/bin/python3

"""class Mylist"""


class MyList(list):
    """class that inherits attributes reference of class list"""

    def print_sorted(self):
        """Method that prints the sorted list"""
        sortlist = self.copy()
        sortlist.sort()
        print(sortlist)
