#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

text = "Last digit of {:d} is ".format(number)
if (number < 0):
    last_digit = -1 * ((number * -1) % 10)
else:
    last_digit = number % 10

text += "{:d} and is ".format(last_digit)

if (last_digit == 0):
    text += "0\n"
elif (last_digit > 5):
    text += "greater than 5\n"
elif (last_digit < 6):
    text += "less than 6 and not 0\n"

print(text, end="\n")

# print("{:d} % 10 = {:d}".format(number, number % 10))
