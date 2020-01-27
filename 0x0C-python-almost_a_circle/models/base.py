#!/usr/bin/python3

"""
module for Base class
"""


import os
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

    @staticmethod
    def from_json_string(json_string):
        """json to string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        if cls.__name__ is "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ is "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = cls.__name__ + ".json"
        if not os.path.isfile(file):
            return []
        with open(file, "r") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]
