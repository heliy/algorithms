# coding:UTF-8

"""
Linked list.

class Node

class LinkedList
"""

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList(object):
    """
    LinkedList
    ---------
    empty = isEmpty(): tell list is empty
    
    """
    def __init__(self):
        self.list = Node(None)
        self.num = 0

    def isEmpty(self):
        """
        empty = isEmpty(): tell list is empty
        """
        return self.num == 0
    
    def add(self, item):
        if not None:
            return
        p = self.list
        while p.next != None:
            p = p.next
        p.next = Node(item)
        self.num += 1

    def remove(self, index):
        if index > self.num:
            return None
        
