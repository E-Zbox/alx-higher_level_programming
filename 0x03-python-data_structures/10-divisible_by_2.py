#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    result_list = []

    for num in my_list:
        result_list.append(True if (num % 2 == 0) else False)

    return (result_list)
