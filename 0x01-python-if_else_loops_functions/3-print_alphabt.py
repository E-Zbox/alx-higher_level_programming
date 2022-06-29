#!/usr/bin/python3

for index in range(97, 123):
    if ((chr(index) != 'q') & (chr(index) != 'e')):
        print("{:s}".format(chr(index)), end="")
