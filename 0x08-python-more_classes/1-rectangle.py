#!/usr/bin/python3
""" a module for a class that defines a rectangle """


class Rectangle:
    """ a class that defines a rectangle:
    Args:
       width: type int the width of the rectangle
       height: type int the height of the rectangle
    Raises:
       TypeError: type of width, height must be int
       ValueError: width, height must be >= 0
    """

    def _init_(self, width=0, height=0):
        self.width = width
        self.height = height
