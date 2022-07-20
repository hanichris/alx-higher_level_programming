#!/usr/bin/python3

"""Module that holds the definition of a Node class and Linked list class."""


class Node:
    """Models a node."""

    def __init__(self, data, next_node=None):
        """Initialize the node.

        Args:
            data (int): value to store in the node.
            next_node (Node): 'pointer' to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrive/set the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Models a singly-linked list."""

    def __init__(self):
        """Initialize the singly-list object."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into the linked list.

        The insert is performed in a manner that maintains the sort order
        of the values within the linked list.

        Args:
            value (int): data to be inserted into the list.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
        else:
            cur = self.__head
            while (cur.next_node is not None and cur.next_node.data <= value):
                cur = cur.next_node
            new.next_node = cur.next_node
            cur.next_node = new

    def __str__(self):
        """Define the print representation of a singly-linked list."""
        data = []
        cur = self.__head
        while cur is not None:
            data.append(str(cur.data))
            cur = cur.next_node
        return '\n'.join(data)
