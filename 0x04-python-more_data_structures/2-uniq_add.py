#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    uniq_list = list()
    uniq_list = list(filter(lambda x:x if (x not in uniq_list) else pass, my_list))
    return (list(reduce(lambda x, y: x + y, uniq_list)))
