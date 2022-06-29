#!/usr/bin/python3

def uppercase(_str):
    delta = ord('a') - ord('A')

    for char in _str:
        if ((ord(char) >= ord('a')) & (ord(char) <= ord('z'))):
            print("{}".format(chr(ord(char) - delta)), end="")
        else:
            print("{}".format(char), end="")

    print("")
