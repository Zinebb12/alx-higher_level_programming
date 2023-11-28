#!/usr/bin/python3

for first_numbers in range(0, 10):
     for second_numbers in range(first_numbers + 1, 10):
       if first_numbers == 8 and second_numbers == 9:
           print("{}{}".format(first_numbers, second_numbers))
       else:
           print("{}{}".format(first_numbers, second_numbers), end=", ")
