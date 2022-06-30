#!/usr/bin/python3
import sys

args = sys.argv
len_args = len(args) - 1

if __name__ == '__main__':
    text = f"{len_args} argument{'s' if len_args != 1 else ''}"
    text += f"{':' if len_args > 0 else '.'}"
    print(text)

    for index in range(1, len_args + 1):
        print(f"{index}: {args[index]}")
