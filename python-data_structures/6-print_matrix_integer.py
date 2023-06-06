#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if matrix is None:
        return

    '''for row in matrix:
        for i, digit in enumerate(row):
            if i != len(row) - 1:
                print("{:d}".format(digit), end=' ')
            else:
                print("{:d}$".format(digit), end='')
        print()'''

    if not matrix:
        return

    for row in matrix:
        if not row:
            return
        else:
            for i, element in enumerate(row):
                if i != len(row) - 1:
                    print("{:d} ".format(element), end='')
                else:
                    print("{:d}$".format(element), end='')
            print()
    print()
