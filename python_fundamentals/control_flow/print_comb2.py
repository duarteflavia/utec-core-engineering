#!/usr/bin/env python3
for i in range(0, 100):
    ending = ", " if i < 99 else "\n"
    print("{0:02d}".format(i), end=ending)
