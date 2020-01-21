#!/usr/bin/python3
"""number of lines"""


def number_of_lines(filename=""):
    """number of lines"""
    i = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            i += 1
        return i
