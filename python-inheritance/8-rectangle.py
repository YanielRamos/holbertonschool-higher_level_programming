#!/usr/bin/python3

"""Module that have a class that inherits from other one"""


class Rectangle(BaseGeometry):
    """class inherited from Basegeometry"""

    def __init__(self, width, height):
        """Method that set width and height private and
        validate that they are positive integers"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
