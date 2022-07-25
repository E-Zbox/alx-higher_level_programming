#!/usr/bin/python3
""" the rectangle module """


class Rectangle:
    """ <class Rectangle> """
    def __init__(self, width=0, height=0):
        """ initialize <class Rectangle> """
        self.__width = width
        self.__height = height

    def __str__(self):
        result = ""

        if ((self.__width == 0) | (self.__height == 0)):
            return (result)

        for row in range(self.__height):
            for col in range(self.__width):
                result += "#"
            if (row != self.__height - 1):
                result += "\n"
        return (result)

    @property
    def width(self):
        """ returns the width property of <class Rectangle> """
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height property of <class Rectangle> """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ returns the height property of <class Rectangle> """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ performs mathematical operation

        Returns:
            area of rectangle

        """
        return (self.__width * self.__height)

    def perimeter(self):
        """ performs mathematical operation

        Returns:
            perimeter of rectangle

        """
        if ((self.__width == 0) | (self.__height == 0)):
            return (0)

        return (2 * (self.__width + self.__height))
