#!/usr/bin/python3

"""function that returns True if object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """function that compares"""
    if isinstance(type(obj), a_class):
        return True
    else:
        return False
