#!/usr/bin/python3
"""Module with a class called Base"""

import json
from os import path

class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """json string method"""
        if isinstance(list_dictionaries, list):
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            else:
                json_string = json.dumps(list_dictionaries)
        return json_string

    def save_to_file(cls, list_objs):
        """save file method"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if list_objs is not None:
            list_dic = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dic)

        with open(filename, 'w') as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instance
        """
        filename = cls.__name__ + '.json'
        if path.exists(filename) is False:
            return []
        with open(filename, 'r') as fd:
            attrs_dic = cls.from_json_string(fd.read())
            li = []
            for i in attrs_dic:
                li.append(cls.create(**i))
            return li
