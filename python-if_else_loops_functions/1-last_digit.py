#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = str(number)[-1:]
if last > "5" and last != 0:
    if number < 0:
        print(
            f"Last digit of {number} is -{last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is greater than 5")
if last == "0":
    print(f"Last digit of {number} is {last} and is 0")
if not last > "0" and last < "6":
    if number < 0:
        print(
            f"Last digit of {number} is -{last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
