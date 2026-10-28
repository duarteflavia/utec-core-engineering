#!/usr/bin/env python3
"""Clase Cuadrado"""


class Square:
    """Representacion del cuadrado"""
    def __init__(self, size = 0):
        if not isinstance(size, int) or isinstance(size, bool):
            raise TypeError("tamano debe ser int")
        if size < 0:
            raise ValueError("tamano deber ser mayor o igual a 0")
        self.__size = size
