#!/usr/bin/python3

"""Module that reads atext file and prints it to stdout"""


def read_file(filename=""):
    file = open(filename)
    content = file.read()
    print(content)
