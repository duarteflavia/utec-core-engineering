#!/usr/bin/env python3
def pow(a, b):
    if b > 0:
        rango = b
        for _ in range(rango):
            res *= a
            
    elif b == 0:
        res = 1

    print(res)
