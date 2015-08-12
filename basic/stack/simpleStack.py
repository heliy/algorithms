# coding: UTF-8

'''

Stack with simple implementation(built-in arraylist).

class Stack
'''

class Stack(object):
    '''
    Stack with simple implementation(built-in arraylist).
    -------------
      Stack(): init queue
      push(item): push an item
      item = pop(): remove the most recently added item
      empty = isEmpty(): tell stack is empty
      stackSize = size(): get size of stack 
      clear(): reset the stack
    '''
    def __init__(self):
        self.array = []
        self.num = 0

    def push(self, item):
        '''
        void push(item): push an item
        input:
          item: item to push
        output:
          None
        '''
        self.array.append(item)
        self.num += 1

    def pop(self):
        '''
        item = pop(): remove the most recently added item
        input:
          None
        output:
          item: item for pop, None if stack is empty
        '''
        if self.isEmpty():
            return None
        else:
            item = self.array.pop()
            self.num -= 1
            return item

    def isEmpty(self):
        '''
        empty = isEmpty(): tell stack is empty
        input:
          None
        output:
          empty: is stack empty, boolean
        '''        
        return self.num == 0

    def size(self):
        '''
        stackSize = size(): get size of stack 
        input:
          None
        output:
          stackSize: size of stack, int
        '''
        return self.num

    def clear(self):
        '''
        clear(): reset the stack
        input/output:
          None
        '''
        self.array = []
        self.num = 0
    
