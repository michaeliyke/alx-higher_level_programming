#!/usr/bin/python3
import sys

av = sys.argv
ac = len(av)
total = 0

if __name__ == "__main__":
    for i in range(1, ac):
        total += int(av[i])
    print("{}".format(total))
