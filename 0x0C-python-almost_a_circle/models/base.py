#!/usr/bin/python3
"""
Base class
"""


import json


class Base:
    """Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file = cls.__name__+".json"
        list = []
        for i in list_objs:
            list.append(cls.to_dictionary(i))
        with open(file, "w") as f:
            f.write(cls.to_json_string(list))
