#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx < 0 | idx >= len(my_list)):
        return (my_list)

    my_list_copy = []
    for index in range(0, len(my_list)):
        print(index)
        if index == idx:
            my_list_copy[idx] = element
        else:
            my_list_copy[index] = my_list[index]

    return (my_list_copy)