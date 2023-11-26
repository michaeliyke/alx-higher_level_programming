#!/usr/bin/python3
"""Write a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to "".
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", end="")
    if first_name:
        print(" {}".format(first_name), end="")
    if last_name:
        print(" {}".format(last_name))
    else:
        print(" ")
