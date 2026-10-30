#!/usr/bin/env python3
"""Clase Square que herede de Rectangle"""

Rectangle = __import__('1-rectangle').Rectangle

class Square(Rectangle):
    """Comportamiento de Square"""
    
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
