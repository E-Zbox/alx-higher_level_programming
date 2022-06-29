#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return (str)

    _str = ""
    for index in range(0, len(str)):
        _str += str[index] if index != n else ""

    return (_str)
