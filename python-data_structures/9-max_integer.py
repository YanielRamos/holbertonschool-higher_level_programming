#!/usr/bin/python3


def max_integer(my_list=[]):

    if my_list is None:
        return None

    max_integer = sorted(my_list, reverse=True)

    return max_integer[0]
