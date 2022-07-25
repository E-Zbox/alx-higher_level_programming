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
        self.__size = size

    @property
    def size(self):
        """ gets the current size """
        return (self.__size)

    @size.setter
    def size(self, size):
        """ sets the current size """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ gets the current size """
        return (self.__size)

    @size.setter
    def size(self, size):
        """ sets the current size """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ compute amd return the current square area
        Returns:
            the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
