#!/usr/bin/env python3
def common_elements(set_1, set_2):
    conjunto_vacio = set()
    for item in len(set_1):
        if item in set_1 & item in set_2:
            conjunto_vacio.append(item)  
