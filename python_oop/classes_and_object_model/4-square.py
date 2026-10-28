#!/usr/bin/env python3
"""clase cuadrao"""


class Square():
    """Setter y Geettters aaa"""
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
