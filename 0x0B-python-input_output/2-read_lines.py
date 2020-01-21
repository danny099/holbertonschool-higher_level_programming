#!/usr/bin/python3
"""read lines"""


def read_lines(filename="", nb_lines=0):
    """read lines"""
    with open(filename, 'r', encoding="utf-8") as f:
        i = 0
        for line in f:
            i += 1
        if nb_lines <= 0 or nb_lines >= i:
            with open(filename, 'r', encoding="utf-8") as f:
                for line in f:
                    print(line, end="")
        else:
            with open(filename, 'r', encoding="utf-8") as f:
                for lines in range(nb_lines):
                    print(f.readline(), end="")
