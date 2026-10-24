#!/usr/bin/env python3
"""Este modulo contiene una funcion para escribe una cadena en un archivo de texto y devuelva el nro de caracteres escritos."""
    def write_file(filename="", text=""):
        with open(filename, "w", encoding="utf-8") as f:
            written = f.write(text)

    print(written)
