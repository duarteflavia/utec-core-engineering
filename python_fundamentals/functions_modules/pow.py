#!/usr/bin/env python3
def pow(a, b):
    res = 1

    if b > 0:
        rango = b
        for _ in range(rango):
            res *= a
    elif b == 0:
        return 1
    elif b < 0:
        return 1 / res

    return res
