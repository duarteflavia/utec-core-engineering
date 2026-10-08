#!/usr/bin/env python3
alfa = ""

for i in range(ord("a"), ord("z") + 1):
    letra = chr(i)
    if letra != 'q' and letra != 'e':
        alfa += letra

print(alfa)
