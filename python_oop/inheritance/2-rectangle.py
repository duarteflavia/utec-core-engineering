#!/usr/bin/env python3
"""Clase Rectangle que herede de BaseGeometry"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representación de un rectángulo"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la representación en cadena del rectángulo."""
        return f"[Rectangle] {self.__width}/{self.__height}"
