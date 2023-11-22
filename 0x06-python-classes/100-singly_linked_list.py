#!/usr/bin/python3
"""Singly Linked List Node
"""


class Node:
    """The Node class
    """

    def __init__(self) -> None:
        self.__data = None
        self.__next_node = None

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        self.__next_node = node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
