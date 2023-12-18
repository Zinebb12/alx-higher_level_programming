#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        number = 0
        for i in range(x):
            print(my_list[i], end="")
            number += 1
            for x in range(number):
                print("", end="")
        print()
        return number
    except IndexError:
        print()
        return number
