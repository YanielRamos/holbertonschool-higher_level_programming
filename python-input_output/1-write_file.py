#!/usr/bin/python3

"""Module of how to write a string to a text file and return
amount of characters written"""


def write_file(filename="", text=""):
    """function that write and counts"""
    with open(filename, "w") as file:
        return file.write(text)
