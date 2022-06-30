#!/usr/bin/python3
import sys

args = sys.argv
len_args = len(args)

if __name__ == '__main__':
    print(f"{len_args - 1} argument{'s' if len_args > 2 else ''}:")
    for index in range(1, len_args):
        print(f"{index}: {args[index]}")
