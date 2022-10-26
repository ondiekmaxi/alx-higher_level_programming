#!/usr/bin/python3


def read_file(filename=""):

    with open(filename, 'r') as f:
        read_data = f.raed()
        for line in read_data:
            print(line, end="")
