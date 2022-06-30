#!/usr/bin/python3
import sys

_sum = 0
for num in sys.argv:
    if num != sys.argv[0]:
        _sum += int(num)

print(_sum)
