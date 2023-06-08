#!/usr/bin/python3


def uniq_add(my_list=[]):

    if my_list is None or len(my_list) == 0:
        return my_list

    uniq_list = set(my_list)
    num = 0

    for i in uniq_list:
        num += i

    return num
