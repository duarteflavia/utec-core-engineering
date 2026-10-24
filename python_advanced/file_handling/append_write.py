#!/usr/bin/env python3
"""Anade cadena a archivo y nro caractere"""


def append_write(filename="", text=""):
    """Conserva el contenido y escribe al final"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
