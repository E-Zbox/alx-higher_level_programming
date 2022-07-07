#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    keys = list(a_dictionary.keys())

    if (key in keys):
        del a_dictionary[key]

    return (a_dictionary)
