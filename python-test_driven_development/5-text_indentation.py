#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """function that prints 2 new lines after [., ?, :] """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbols = [".", "?", ":"]

    skip_space = False

    for char in text:
        if skip_space:
            if char != " ":
                print(char, end="")
                skip_space = False
        elif char in symbols:
            print(f"{char}\n", end="\n\n")
            skip_space = True
        else:
            print(char, end="")
