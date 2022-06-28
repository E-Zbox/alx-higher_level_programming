#!/usr/bin/python3

for number in range(100):
	if (number != (100 - 1)):
		print("{:0>2}".format(number), end=", ")
	else:
		print("{:0>2}".format(number), end="\n")
