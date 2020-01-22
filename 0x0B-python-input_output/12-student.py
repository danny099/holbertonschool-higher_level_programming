#!/usr/bin/python3
"""class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for i in attrs:
            try:
                dic[i] = self.__dict__[i]
            except:
                pass
        return dic
