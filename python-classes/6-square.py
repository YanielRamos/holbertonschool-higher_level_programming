#!/usr/bin/python3

"""
module: 6-square
class Square
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        defining size to square and position
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        return the area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        printing the output
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)

    @property
    def size(self):
        """
        returning the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        defining size to square if value is
        an int and bigger than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        returning the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        defining the position if value is a tuple of 2 with only integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
