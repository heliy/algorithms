# coding: UTF-8

'''
class SimpleStack: Stack with simple implementation(built-in arraylist).
'''

class SimpleStack(object):
    '''
    Stack with simple implementation(built-in arraylist).
    -------------
      Stack(): init queue
      push(item): push an item
      pop(): remove the most recently added item
      top(): get the most recently added item
      empty = isEmpty(): tell stack is empty
      stackSize = size(): get size of stack 
      clear(): reset the stack
    '''
    def __init__(self):
        self.array = []
        self.num = 0

    def push(self, item):
        '''
        push an item
        input:
          item: item to push
        output:
          None
        '''
        # print "push:", item
        self.array.append(item)
        self.num += 1

    def pop(self):
        '''
        remove the most recently added item
        input/output:
          None
        '''
        if not self.isEmpty():
            item = self.array.pop()
            # print "pop:", item
            self.num -= 1

    def top(self):
        '''
        get the most recently added item
        input:
          None
        output:
          item: the most recentlu added item, None otherwise
        '''
        if not self.isEmpty():
            return self.array[-1]

    def isEmpty(self):
        '''
        tell stack is empty
        input:
          None
        output:
          empty: is stack empty, boolean
        '''        
        return self.num == 0

    def size(self):
        '''
        get size of stack 
        input:
          None
        output:
          stackSize: size of stack, int
        '''
        return self.num

    def clear(self):
        '''
        reset the stack
        input/output:
          None
        '''
        self.array = []
        self.num = 0
    
