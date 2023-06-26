#!/usr/bin/python3
"""Module with a class called Base"""


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances"""
        if id is None:
            Base.__nb_objects += 1
            id += Base.__nb_objects
            self.id = id
        else:
            self.id = id
