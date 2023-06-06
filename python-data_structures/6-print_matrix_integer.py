#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix is None:
        return

    for row in matrix:
        for i, digit in enumerate(row):
            if i != len(row) - 1:
                print("{:d}".format(digit), end=' ')
            else:
                print("{:d}$".format(digit), end='')
        print()
