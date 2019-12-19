#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = a_dictionary.copy()
    for i in mult:
        mult[i] = a_dictionary[i] * 2
    return mult
