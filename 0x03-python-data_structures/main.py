#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL("./libPyList.so")
lib.print_python_list_info.argtypes = [ctypes.py_object]

l = ["One", "Two", "Three", "Four"]

lib.print_python_list_info(l)
