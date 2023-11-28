#!/usr/bin/python3
def copy_list(l):
    return l.copy() if type(l) is list or type(l) is dict else l
