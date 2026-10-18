#!/usr/bin/env python3
def pow(a, b):
    if b > 0:
        for i in range(b+1):
            res = 1 * a
            i += 1
    elif b == 0:
        res = 1

    print(f"{res}", end="")
