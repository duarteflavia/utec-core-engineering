#!/usr/bin/env python3
def pow(a, b):
    if b > 0:
        rango = b+1
        for i in range(rango):
            res = a * a
            i += 1
    elif b == 0:
        res = 1

    print(f"{res}", end="")
