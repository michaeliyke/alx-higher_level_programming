#!/usr/bin/python3
"""
Write a function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """function that prints text with indentation

    Args:
        text (str): str text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()

    s = ""
    for c in text:
        if c in " \n\t\v" and s == "":  # detect the start of a collection
            continue

        s += c  # collect char tokens
        if c in ".?:":
            print(s, end="\n\n")  # print collected tokens and start afresh
            s = ""

    if s:  # print any remaining characters beyond the separartors
        print(s)
