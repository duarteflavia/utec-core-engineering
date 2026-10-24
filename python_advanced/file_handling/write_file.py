#!/usr/bin/env python3
"""Escribe una cadena en un archivo y devuelve el nro de caracteres escritos."""


def write_file(filename="", text=""):
    """Escribe un archivo y lee la cant de caracteres"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
