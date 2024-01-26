#!/usr/bin/python3
# 100-singly_linked_list.py by Dalhatmd
""" A node definition """


class Node:
    """ Node class definition """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        """ property getter for next_nodr """

        return (self._next_node)

    @next_node.setter
    def next_node(self, value):
        """ next_mode setter """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self._next_node = value

    @property
    def data(self):
        """ data getter """

        return (self._data)

    @data.setter
    def data(self, value):
        """ data setter """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value


class SinglyLinkedList:
    """ Singly linked list class """
    def __init__(self):
        """initialiser for the class """

        self.head = None

    def sorted_insert(self, value):
        """ inserts a node in a sorted manned """

        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """ Makes linked list printable"""

        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next_node
        return '\n'.join(map(str, result))
