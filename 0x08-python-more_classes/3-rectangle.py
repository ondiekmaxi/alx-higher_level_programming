#!/usr/bin/python3
""" a module for a class that  defines a rectangle """


class Rectangle:
    def _init_(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError
        if value < 0:
            raise ValueError
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError
        if value < 0:
            raise ValueError
        self._height = value

    def area(self):
        return self._width * self._height

    def perimrter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return (2 * self._width) + (2 * self._height)

    def _str_(self):
        if self._width == 0 or self._height == 0:
            return ""
        return (("#" * self._width + "\n") * (self._height))[:-1]
