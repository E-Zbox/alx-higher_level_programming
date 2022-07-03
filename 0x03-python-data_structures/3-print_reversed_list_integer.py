#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    len_my_list = len(my_list) - 1
    for index in range(len_my_list, -1, -1):
        print("{:d}".format(my_list[index]))
