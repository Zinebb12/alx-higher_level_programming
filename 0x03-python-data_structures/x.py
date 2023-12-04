def max_integer(my_list=[]):
    i = 0
    j = 1
    max_value = 0
    if len(my_list) == 0:
	return None
    elif len(my_list) == 1:
        return my_list[i]


    while i <= len(my_list) and j < len(my_list):
        if (my_list[i] >= my_list[j]) and (my_list[i] >= max_value):
            max_value = my_list[i]
	elif (my_list[j] >= my_list[i]) and (my_list[j] >= max_value):
            max_value = my_list[j]
	i += 1 
	j += 1
    return max_value
