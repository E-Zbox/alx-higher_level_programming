#!/usr/bin/python3
"""The Square module docstrings.
This module demonstrates creating a Square class and atrributes
File calling:
        $ python3 0-square.py
"""


class Square:
    """ creates an empty Square class  defining a class """

    def __init__(self, size=0, position=(0, 0)):
        """docstring on the __init__ method.
        Args:
            size (str): the size of the square
        """
        self.size = size
        self.position = position

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
    def position(self):
        """ gets the current position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """ sets the current position for square cordinate.
        Args:
            value (tuple): tuple of 2 positive integers
        Raises:
            TypeError: if value is not tuple of 2 positive integers
        """

        err = TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value, tuple):
            raise err
        elif len(value) != 2:
            raise err
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise err
        elif value[0] < 0 or value[1] < 0:
            raise err
        else:
            self.__position = value

    def area(self):
        """ compute and return the current square area
        Returns:
            the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """ prints the square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square = Square(3, -20)
    my_square.my_print()
    print("--")
