#!/usr/bin/python3
def no_c(my_string):
    charslist = list(my_string)
    for char in charslist:
        if char == 'c' or char == 'C':
            charslist.remove(char)
    return("".join(charslist))
