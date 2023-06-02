#!/usr/bin/python3
import sys

if __name__ == "__main__":

    args = sys.argv[1:]
    args_counter = len(args)

    if args_counter == 0:
        print("{} arguments.".format(args_counter))
    elif args_counter == 1:
        print("{} argument:".format(args_counter), end="\n")
        print(f"{args_counter}:", "".join(args), end="\n")
    else:
        print(f"{args_counter} arguments:", end="\n")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}", end="\n")
