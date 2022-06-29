#!/usr/bin/python3

def uppercase(_str):
    delta = ord('a') - ord('A')
    text = ""

    for char in _str:
        if ((ord(char) >= ord('a')) & (ord(char) <= ord('z'))):
            text += "{}".format(chr(ord(char) - delta))
        else:
            text += "{}".format(char)

    print(text)
