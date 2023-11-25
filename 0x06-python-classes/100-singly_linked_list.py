#!/usr/bin/python3
"""Singly Linked List Node
"""


class Node:
    """The Node class
    """

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

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


class SinglyLinkedList:
    """Singly linked list
    """

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        h = self.head  # self.head
        while h:
            print(h.data)
            h = h.next_node

    def insert_sorted(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            h = self.head
            while h:
                h = h.next_node
