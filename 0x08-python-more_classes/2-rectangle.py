#!/usr/bin/python3
""" the rectangle module """


class Rectangle:
    """ <class Rectangle """
    def __init__(self, width=0, height=0):
        """ <class Rectangle> intialization"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns width property of <class Rectangle> """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ instantiate width property of <class Rectangle> """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height property of <class Rectangle> """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ instantiate height property of <class Rectangle> """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ performs mathematical operation

        Returns:
            product of width and height

        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ performs mathematical operation

        Returns:
            product of 2 and the sum of width and height

        """
        if ((self.__width == 0) | (self.__height == 0)):
            return (0)
        return (2 * (self.__width + self.__height))
