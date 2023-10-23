#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    list_len = 0
    count = 0
    for item in my_list:
        list_len += 1
    try:
        if (x == 0):
            return elements
        if (x >= list_len):
            for elem in my_list:
                print("{}".format(elem), end="")
            print()
            return list_len
        else:
            for elem in my_list:
                elements += 1
                print("{}".format(elem), end="")
                if (elements == x):
                    break
            print()
            return elements
    except BaseException:
        pass
