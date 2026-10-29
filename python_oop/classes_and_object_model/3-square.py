#!/usr/bin/env python3
"""clase cuadrao"""


class Square:
    """Tamano y area"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2
