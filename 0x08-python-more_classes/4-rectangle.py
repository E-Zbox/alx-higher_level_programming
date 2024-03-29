#!/usr/bin/python3
""" the Rectangle module """


class Rectangle:
    """ <class Rectangle> """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        shape = ""
        if ((self.__width == 0) | (self.__height == 0)):
            return (shape)
        for row in range(self.__height):
            for col in range(self.__width):
                shape += "#"
            if (row != (self.__height - 1)):
                shape += "\n"

        return (shape)

    @property
    def width(self):
        """ returns width property """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ instantiates width property """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height property """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ instantiates height property """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = height

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
        res = 2 * (self.__width + self.__height)
        return (0 if ((self.__width == 0) | (self.__height == 0)) else (res))
