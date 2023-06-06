#!/usr/bin/python3


def no_c(my_string):

    if my_string is None:
        return

    new_string = my_string.replace('c', "").replace('C', "")
    return new_string
