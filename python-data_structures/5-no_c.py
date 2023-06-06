#!/usr/bin/python3


def no_c(my_string):

    if my_string is None:
        return

    new_stirng = my_string.replace('c', "").replace('C', "")
    return new_stirng
