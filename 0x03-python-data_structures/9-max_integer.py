#!/usr/bin/python3

def max_integer(my_list=[]):
    len_my_list = len(my_list)

    if (len_my_list == 0):
        return (None)

    _max = my_list[0]
    for index in range(1, len_my_list):
        _max = my_list[index] if (my_list[index] > _max) else _max

    return (_max)
