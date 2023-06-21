#!/usr/bin/python3

"""module that writes and object to a text file"""

import json


def save_to_jsoin_file(my_obj, filename):
    """function that writes a json object the file"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
