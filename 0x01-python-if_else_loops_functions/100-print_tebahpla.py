#!/usr/bin/python3

for num in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(num) if (num % 2 == 0) else chr(num - 32)), end="")
