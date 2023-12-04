def add_tuple(tuple_a=(), tuple_b=()):
    result_a = ()
    result_b = ()
#checking to tuple a if we can access it
    if len(tuple_a) >= 2:
        result_a = tuple_a[0] + tuple_a[1]
    elif len(tuple_a) < 2:
        result_a = (0, 0)
#checking to tuple b if we can access it
    if len(tuple_b) >= 2:
        result_b = tuple_b[1] + tuple_b[0]
    elif len(tuple_b) < 2:
        result_b = (0, 0)
#add the elements of each tuple with results
    return (result_a, result_b)
