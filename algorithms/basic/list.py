# coding: UTF-8

"""
# Node in list.
class SingleNode: with single pointer to next node.
class DoubleNode: with two pointers linked to next and perivous nodes respectively.

# Linked list.
class LinkedList

"""

class SingleNode(object):
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class DoubleNode(object):
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.next = prev
        self.prev = next

class LinkedList(object):
    """
    LinkedList
    ---------
    empty = isEmpty(): tell list is empty.
    addHead(item): insert at the beginning.
    addTail(item): insert at the ending.
    node = get(index): get item at index(begin in 0).
    index = index(item): get index of that item.
    item = remove(index): remove the node in index.
    size = size(): size of list.
    """
    def __init__(self):
        self.list = SingleNode(None)
        self.num = 0

    def isEmpty(self):
        """
        empty = isEmpty(): tell list is empty.
        input: None
        output: boolean
        """
        return self.num == 0

    def addHead(self, item):
        """
        addHead(item): insert at the beginning.
        input:
          item
        output: None
        """
        self.list.next = SingleNode(item, self.list.next)
        self.num += 1
    
    def addTail(self, item):
        """
        addTail(item): insert at the ending.
        input:
          item
        output: None
        """
        p = self.list
        while p.next is not None:
            p = p.next
        p.next = SingleNode(item)
        self.num += 1

    def get(self, index):
        """
        node = get(index): get item at index(begin in 0).
        input:
          index: 0, 1, .., numbers_of_node-1
        output:
          node: node in node_of_index, None if index is invalid.
        """
        if index < 0 or index >= self.num:
            return None
        p = self.list.next
        for i in range(self.num):
            if i == index:
                return p
            else:
                p = p.next

    def index(self, item):
        """
        index_num = index(item): get index of that item.
        input:
          item
        output:
          index_num: index of item, None if not found.
        """
        p = self.list.next
        for i in range(0, self.num):
            if p.item == item:
                return i
            else:
                p = p.next
        return None
    
    def remove(self, index):
        """
        item = remove(index): remove the node in index.
        input:
          index: index of node you want to remove.
        output:
          item: item in that index, None if index is invalid.
        """
        if index < 0 or index >= self.num:
            return None
        prev, p = self.list, self.list.next
        for i in range(self.num):
            if i == index:
                prev.next = p.next
                self.num -= 1
                return p.item
            else:
                prev = p
                p = p.next        

    def size(self):
        """
        size = size(): size of list.
        input: None.
        output:
          size
        """
        return self.num
    
    def __str__(self):
        if self.isEmpty():
            return "Empty List."
        n = self.list.next
        s = str(n.item)
        while n.next is not None:
            n = n.next
            s += " -> "
            s += str(n.item)
        return s
