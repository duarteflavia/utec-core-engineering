#!/usr/bin/env python3
"""clase cuadrao"""


class Square():
    """Setter y Geettters aaa"""
    def __init__(self, size = 0):
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
