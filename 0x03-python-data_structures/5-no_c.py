#!/usr/bin/python3

def no_c(my_string):
    new_string = ""

    for _str in my_string:
        new_string += _str if ((_str != 'c') and (_str != 'C')) else ''

    return (new_string)
