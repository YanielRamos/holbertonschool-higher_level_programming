#!/usr/bin/python3
import json

"""module that returns a JSON representation of an object"""


def to_json_string(my_obj):
    """function that converts and object to a json string"""
    json_string = json.dumps(my_obj)
    return json_string
