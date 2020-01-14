#!/usr/bin/python3
""" add
two
integers
a + b
"""


def add_integer(a, b=98):
    """ add
    two
    integers"""
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a + b)
