#!/usr/bin/env python3
def uppercase(str):
    resultado = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            caracter_mayus = chr(ord(c) - 32)
            resultado += caracter_mayus
        else:
            resultado += c

    print("{}".format(resultado))
