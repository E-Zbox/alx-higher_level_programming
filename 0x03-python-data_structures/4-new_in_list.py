#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if ((idx < 0) or (idx >= len(my_list))):
        return (my_list)

    my_list_copy = []
    for index in range(len(my_list)):
        if index == idx:
            my_list_copy.append(element)
        else:
            my_list_copy.append(my_list[index])

    return (my_list_copy)
