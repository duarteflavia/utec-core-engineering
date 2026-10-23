#!/usr/bin/env python3
def raise_exception():
    try:
        int("hello")
    except (ValueError):
        print("valor no valido")
