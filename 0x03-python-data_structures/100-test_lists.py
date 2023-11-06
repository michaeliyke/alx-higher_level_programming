#!/usr/bin/python3
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
temp = ['hello', 'World']
lib.print_python_list_info(temp)
del temp[1]
lib.print_python_list_info(temp)
temp = temp + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(temp)
temp = []
lib.print_python_list_info(temp)
temp.append(0)
lib.print_python_list_info(temp)
temp.append(1)
temp.append(2)
temp.append(3)
temp.append(4)
lib.print_python_list_info(temp)
temp.pop()
lib.print_python_list_info(temp)
