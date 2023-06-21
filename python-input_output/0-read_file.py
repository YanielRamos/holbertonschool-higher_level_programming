#!/usr/bin/python3

"""Module that reads atext file and prints it to stdout"""


def read_file(filename=""):
    """function that read and print"""
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
