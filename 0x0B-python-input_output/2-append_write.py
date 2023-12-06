#!/usr/bin/
"""File append module"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    returns the number of characters added"""
    with open(filename, mode="a", encoding="utf-8") as file_:
        file_.write(text)
