#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
info = "Last digit of {:d} is {:d} and is"
if number < 0:
    number_copy = number * -1
    las_dgt = number_copy % 10
    las_dgt *= -1
else:
    las_dgt = number % 10
if las_dgt > 5:
    print(info.format(number, las_dgt), "greater than 5")
if las_dgt == 0:
    print(info.format(number, las_dgt), "0")
if las_dgt < 6 and las_dgt != 0:
    print(info.format(number, las_dgt), "less than 6 and not 0")
