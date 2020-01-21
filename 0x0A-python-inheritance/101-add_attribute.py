#!/usr/bin/python3
"""class"""


def add_attribute(obj, att, val):
    """class"""
    if not(hasattr(obj, '__dict__')):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
