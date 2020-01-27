#!/usr/bin/python3

"""
module for Base class
"""


import json


class Base:
    """one base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init a base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to jsdon function"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save function"""
        file = cls.__name__+".json"
        list = []
        if list_objs:
            for i in list_objs:
                list.append(cls.to_dictionary(i))
            with open(file, "w") as f:
                f.write(cls.to_json_string(list))
