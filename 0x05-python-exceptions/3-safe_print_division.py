#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        r = None
    finally:
        prefix = "Inside result"
        if r == None:
            print("{}: {}".format(prefix, r))
        else:
            print("{}: {:.1f}".format(prefix, r))
        return r
