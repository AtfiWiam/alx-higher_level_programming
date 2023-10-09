#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        b = 1
        for c in a:
            if b == len(a):
                print("{:d}".format(c), end="")
            else:
                print("{:d}".format(c), end=" ")
            b = l + 1
        print()
