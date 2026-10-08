#!/usr/bin/env python3
for i in range(1, 90):
    decenas = i // 10
    unidades = i % 10
    if decenas < unidades:
        ending = "\n" if i == 89 else ", "
        print("{0:d}{1:d}".format(decenas, unidades), end=ending)
