#!/usr/bin/python3
"""apeend write"""


def append_write(filename="", text=""):
    """append write"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
