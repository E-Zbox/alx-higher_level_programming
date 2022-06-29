#!/usr/bin/python3

for num1 in range(10):
    for num2 in range(num1 + 1, 10):
        print("{:d}{:d}".format(num1, num2), end=", ") if num1 != (10 - 2) else print("{:d}{:d}".format(num1, num2))
