#!/usr/bin/python3

for dgt1 in range(10):
    for dgt2 in range(dgt1 + 1, 10):
        print("{:d}{:d}".format(dgt1, dgt2), end=", ")
print()
