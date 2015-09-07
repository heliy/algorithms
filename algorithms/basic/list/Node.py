# coding: UTF-8

"""
Node in linked list.

class SingleNode: with single pointer to next node.

class DoubleNode: with two pointers linked to next and perivous nodes respectively.

"""

class SingleNode(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

class DoubleNode(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None
        self.prev = None

    
