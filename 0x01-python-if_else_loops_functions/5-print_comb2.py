#!/usr/bin/python3

for a in range(100):
    if (a != 99):
        print("{a:02}".format(a=a), end=", ")
    else:
        print("{a:02}".format(a=a))
