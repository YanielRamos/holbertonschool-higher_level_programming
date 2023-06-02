#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    words = dir(hidden_4)
    filtered_words = []

    for name in words:
        if not name.startswith('__'):
            filtered_words.append(name)

    filtered_words.sort()

    for name in filtered_words:
        print(name)
