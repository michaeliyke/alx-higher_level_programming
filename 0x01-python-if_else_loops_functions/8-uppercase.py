#!/usr/bin/python3

def toupper(c):
    x = ord(c)
    if x >= 97 and x <= 122:
        return chr(x - 32)
    return (c)


def uppercase(str):
    for c in str:
        print(toupper(c), end="")
    print()
