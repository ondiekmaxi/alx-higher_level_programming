#!/usr/bin/python3


class MyInt(int):

    def __eq__(self, next):
        return super().__ne__(next)

    def __ne__(self, next):
        return super().__eq__(next)
