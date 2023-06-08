#!/usr/bin/python3


def uniq_add(my_list=[]):

    if my_list is None:
        return

    if len(my_list) == 0:
        return my_list

    unique_int = set()
    result = 0

    for i in my_list:
        if i not in unique_int:
            unique_int.add(i)
            result += i

    return result
