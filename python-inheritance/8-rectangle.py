#!/usr/bin/python3

"""Module that have a class that inherits from other one"""


class Rectangle(BaseGeometry):
    """class inherited from Basegeometry"""

    def __init__(self, width, height):
        """Method that set wight and height private"""
        self.__width = width
        self.__height = height
