#!/usr/bin/python3
"""The Square module docstrings.
This module demonstrates creating a Square class and atrributes
File calling:
        $ python3 0-square.py
"""


class Square:
    """ creates an empty Square class  defining a class """

    def __init__(self, size=0):
        """docstring on the __init__ method.
        Args:
            size (str): the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
