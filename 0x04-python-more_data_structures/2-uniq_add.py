#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    return (reduce(lambda x, y: x + y, uniq_list))
