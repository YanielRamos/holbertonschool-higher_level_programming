#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Module that have a class that inherits from other one"""


class Rectangle(BaseGeometry):
    """class inherited from Basegeometry"""

    def __init__(self, width, height):
        """Method that set width and height private and
        validate that they are positive integers"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
