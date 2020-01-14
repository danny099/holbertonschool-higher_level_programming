#!/usr/bin/python3
"""
text
identation
=)
"""


def text_indentation(text):
    """text
    identation
    =)"""

    if isinstance(text, str):
        symbol = ['.', '?', ':']
        lau = 0
        for i, j in enumerate(text):
            if j in symbol:
                print(text[lau:i + 1].strip() + "\n")
                lau = i + 1
        print(text[lau:].strip(), end='')
    if not isinstance(text, str):
        raise TypeError('text must be a string')
