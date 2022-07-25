#!/usr/bin/python3
"""The Square module docstrings.
This module demonstrates creating a Square class and atrributes
File calling:
        $ python3 0-square.py
"""


class Square:
    """ creates an empty Square class  defining a clas """

    def __init__(self, size):
        """docstring on the __init__ method.
        Args:
            size (str): the size of the square
        """
        self.__size = size
