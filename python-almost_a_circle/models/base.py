#!/usr/bin/python3
"""Module with a class called Base"""

import json


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
