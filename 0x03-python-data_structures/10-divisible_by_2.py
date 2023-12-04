#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    r_list = my_list[:]
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            r_list[i] = 1
        else:
            r_list[i] = 0
    return r_list
