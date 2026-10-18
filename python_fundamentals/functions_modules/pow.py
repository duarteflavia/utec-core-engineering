#!/usr/bin/env python3
def pow(a, b):
    if b == 0:
        return 1

    res = 1
    rango = abs(b)
    for _ in range(rango):
            res *= a

    if b < 0:
        return 1 / res

    return res
