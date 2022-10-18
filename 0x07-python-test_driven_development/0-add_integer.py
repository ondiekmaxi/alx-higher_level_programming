#!/usr/bin/python3
""" a module contains add_integer function
   b = 89 by default at least one arg is required
   raises a TypeError if a, b are not integers or float
   a, b will be casted to integers if they are float
"""


def add_integer(a, b=98):
    if type(a) not n [int, float]:
        raise TypeError("a must be an integer")
    if tybe(b) not in[int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    """returns an integr sum of a + b """
    return a + b
