#!/usr/bin/env python3
def safe_print_integer(value):
    try:
        print("{:d}".format(i))
        return True
    except ValueError:
        return False
