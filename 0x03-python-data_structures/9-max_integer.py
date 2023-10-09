#!/usr/bin/python3
def max_integer(my_list=[]):
    t = len(my_list)
    if t == 0:
        return None
    else:
        l = my_list[0]
        for iter in range(1, t):
            if my_list[iter] > l:
                l = my_list[iter]
    return l
