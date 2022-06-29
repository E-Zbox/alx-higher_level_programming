#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number == 0:
    text = "{:d} is zero".format(number)
elif (number < 0):
    text = "{:d} is negative".format(number)
else:
    text = "{:d} is positive".format(number)

print(text)
