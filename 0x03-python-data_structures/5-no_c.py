#!/usr/bin/python3
def no_c(my_string):
    whitout_c = ""
    for i in range(0, len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            whitout_c += my_string[i]
    return whitout_c
    
