#!/usr/bin/python3
""" a module for a class that defines a rectangle """


class Rectangle:
    """ a class that defines a rectangle with area,
        and perimeter methods:
        Args:
            width: type int the width of the rectangle
            height: type int the height of the rectangle
        Raises:
            TypeError: type of width, height must be int
            ValueError: width, height must be >= 0
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2* self.__width) + (2 * self.__height)

                                                                                                                                                                                                                                                                                                                Footer
