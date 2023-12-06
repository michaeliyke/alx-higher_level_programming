#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            print(line, end="")
