#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = []
    for index in range(1, len(sys.argv)):
        args.append(int(sys.argv[index]))

    print(sum(args))
