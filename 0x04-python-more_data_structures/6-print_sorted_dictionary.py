#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()

    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
