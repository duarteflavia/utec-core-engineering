#!/usr/bin/env python3
"""Funcion q escribe una cadena en un archivo de texto, devuelve el nro de caracteres escritos."""


def write_file(filename="", text=""):
    """Escribe un archivo y lee la cant de caracteres"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
