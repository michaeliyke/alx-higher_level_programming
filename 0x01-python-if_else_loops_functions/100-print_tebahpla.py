#!/usr/bin/python3
i = False
for c in "zyxwvutsrqponmlkjihgfedcba":
    c = c.upper() if i else c
    print("{}".format(c), end="")
    i = not i
