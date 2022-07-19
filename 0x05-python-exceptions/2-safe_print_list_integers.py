#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    #print(f"[{x}] -> {my_list}")
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            count += 1
        except (ValueError, TypeError):
            #print(f"\n{count} >> {my_list[num]}\n")
            continue
        except IndexError:
            break

    print()
    return (count)
