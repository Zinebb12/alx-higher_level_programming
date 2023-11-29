#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for index, i in enumerate(str):
        if index != n:
            result += i
        elif n < 0:
            return str
    return result
