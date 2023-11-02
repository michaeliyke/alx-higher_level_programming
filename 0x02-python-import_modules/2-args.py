#!/usr/bin/python3
from sys import argv as args
ac = len(args)

if __name__ == "__main__":
    if len(args) > 1:
        if len(args) == 2:
            print("{} argument:".format(ac-1))
        else:
            print("{} arguments:".format(ac-1))
    else:
        print("{} arguments.".format(ac-1))

    for i in range(1, ac):
        print("{}: {}".format(i, args[i]))
