#!/usr/bin/python3
"""Module tha have a class Square that inherits form Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes istances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
