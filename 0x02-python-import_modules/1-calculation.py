#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == '__main__':
    print("{} + {} = {}".format(a, b, a + b))
    print("{} - {} = {}".format(a, b, a - b))
    print("{} * {} = {}".format(a, b, a * b))
    print("{} / {} = {}".format(a, b, a / b))
