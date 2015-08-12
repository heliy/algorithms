# coding: UTF-8

'''

Queue with simple implementation(built-in arraylist).

class Queue
'''

class Queue(object):
    '''
    Queue with simple implementation(built-in arraylist).
    ----------
      Queue(): init queue
      void enqueue(item): add an item
      item dequeue(): remove the least recently added item
      bool isEmpty(): is queue empty
      int size(): number of items in queue
      void clear(): clear the queue
    '''
    def __init__(self):
        self.array = []
        self.num = 0

    def enqueue(self, item):
        '''
        enqueue(item)
        input:
          item: item to enqueue
        output:
          None
        '''
        self.array.append(item)
        self.num += 1

    def dequeue(self):
        '''
        item = dequeue()
        input:
          None
        output:
          item: the least recently added item, None if empty
        '''
        if self.isEmpty():
            return None
        item = self.array[0]
        self.array.remove(item)
        self.num -= 1
        return item

    def isEmpty(self):
        '''
        empty = isEmpty()
        input:
          None
        output:
          empty: is queue empty, boolean
        '''
        return self.num == 0

    def size(self):
        '''
        queueSize = size()
        input:
          None
        output:
          queueSize: size of queue, int
        '''
        return self.num

    def clear(self):
        '''
        clear()
        input:
          None
        output:
          None
        '''
        self.array = []
        self.num = 0
    
