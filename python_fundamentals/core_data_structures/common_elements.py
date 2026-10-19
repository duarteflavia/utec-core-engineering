#!/usr/bin/env python3
def common_elements(set_1, set_2):
    conjunto = set()
    for item in set_1:
        if item in set_1 & item in set_2:
            conjunto.add(item)  
    return conjunto
