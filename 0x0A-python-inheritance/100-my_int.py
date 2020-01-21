#!/usr/bin/python3
"""class."""


class MyInt(int):
    """class"""
    def __ne__(self, thing):
        return super().__eq__(thing)

    def __eq__(self, thing):
        return super().__ne__(thing)
