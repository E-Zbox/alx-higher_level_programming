#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for num in range(x):
            print(my_list[num], end='')
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return (count)
