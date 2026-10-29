#!/usr/bin/env python3
"""Clase Rectangle que herede de BaseGeometry"""


class Rectangle(BaseGeometry): 
    """representacion de un rectángulo"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height 
