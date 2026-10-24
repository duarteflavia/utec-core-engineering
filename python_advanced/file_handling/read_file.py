#!/usr/bin/env python3
"""Este modulo contiene una funcion para leer e imprimir archivos de texto."""

def read_file(filename=""):
    """Lee un archivo de texto en formato UTF-8 y lo imprime en stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
