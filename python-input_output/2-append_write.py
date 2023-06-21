#!/usr/bin/python3

"""module have a function that appends a string at the
end of a text file"""


def append_write(filename="", text=""):
    """function that appends a text"""
    with open(filename, "a") as file:
        return file.append(text)
