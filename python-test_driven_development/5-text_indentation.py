#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """function that indent text"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]

    for char in text:
        print(char, end="")
        if char in punctuation_marks:
            print("\n\n", end="")
