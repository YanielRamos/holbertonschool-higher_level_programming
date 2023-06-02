#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    add_result = add(a, b)
    print("{} + {} = {}".format(a, b, add_result), end="\n")

    sub_result = sub(a, b)
    print("{} - {} = {}".format(a, b, sub_result), end="\n")

    mul_result = mul(a, b)
    print("{} * {} = {}".format(a, b, mul_result), end="\n")

    div_result = div(a, b)
    print("{} / {} = {}".format(a, b, div_result), end="\n")
