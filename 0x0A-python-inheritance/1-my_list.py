#!/usr/bin/python3

class MyList(list):
    def print_sorted(self):
        _sorted_list = self[:]
        return (_sorted_list.sort())
