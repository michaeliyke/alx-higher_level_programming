#!/usr/bin/python3


def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    except Exception:
        pass
    finally:
        if r:
            print("Inside result: {:.1f}".format(r))
        else:
            print("Inside result {}".format(r))
    return r
