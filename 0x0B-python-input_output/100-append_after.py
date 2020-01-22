#!/usr/bin/python3
"""append after"""


def append_after(filename="", search_string="", new_string=""):
    """append after"""
    lines = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            lines += line
            if search_string in line:
                lines += new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(lines)
