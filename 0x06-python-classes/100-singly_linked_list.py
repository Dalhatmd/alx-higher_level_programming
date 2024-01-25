#!/usr/bin/python3
# 100-singly_linked_list.py by Dalhatmd
""" A node definition """


class Node:
    def __init__(self, data, next_node= None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self_value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

class SinglyLinkedList:
    def __init__(self):
        pass
    def sorted_insert(self, value):

