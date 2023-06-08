#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    keys_order = sorted(a_dictionary.keys())

    for i in keys_order:
        print("{}: {}".format(i, a_dictionary[i]))
