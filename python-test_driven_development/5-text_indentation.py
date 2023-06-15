#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """function that prints 2 new lines after [., ?, :] """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbols = [".", "?", ":"]

    for char in text:
        if char in symbols:
            print(f"{char}\n", end="\n")
        else:
            print(char, end="")
