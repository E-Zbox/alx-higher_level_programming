#!/usr/bin/python3

for count in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(count) if (count % 2 == 0) else chr(count - 32)), end="")
