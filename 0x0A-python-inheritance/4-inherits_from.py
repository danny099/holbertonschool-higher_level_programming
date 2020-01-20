#!/usr/bin/python3
"""class"""


def inherits_from(obj, a_class):
    """function"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
