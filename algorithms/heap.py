#coding: UTF-8

__all__ = [
    'Heap',
    ]

from utils import isLessThan, isMoreThan

class Heap(object):
    '''
    (min- / max-)Heap
    -----
    refer to [CLRS]-6
    '''
    def __init__(self, initData=None, isMaxHeap=True):
        self.isMaxHeap = isMaxHeap
        self.func = isMaxHeap and isMoreThan or isLessThan
        if initData is None:
            self.data = [None]
        else:
            self.data = [None] + initData
            self.build()

    def __get(self, index=1):
        if index <= 0 or index > self.num():
            return None
        else:
            return self.data[index]

    def top(self):
        return self.__get()

    def num(self):
        return len(self.data) - 1

    def parent(self, i):
        return i//2

    def left(self, i):
        return i*2 if 1 <= i*2 <= self.num() else None

    def right(self, i):
        return i*2+1 if 1 <= i*2+1 <= self.num() else None

    def heapify(self, index):
        if index <= 0 or index > self.num():
            return
        
        l = self.left(index)
        r = self.right(index)
        m = index
        if l is not None and self.func(self.__get(l), self.__get(m)):
            m = l
        if r is not None and self.func(self.__get(r), self.__get(m)):
            m = r
        if  m != index:
            self.data[index], self.data[m] = self.data[m], self.data[index]
            self.heapify(m)

    def up(self, index):
        self.heapify(index)
        while index >= 1:
            index = self.parent(index)
            self.heapify(index)

    def add(self, x):
        self.data.append(x)
        self.up(self.num())

    def build(self):
        for i in range(self.num()//2, 0, -1):
            self.heapify(i)
        
        
class priorityQueue(object):
    def __init__(self, isMaxPriority=True):
        self.isMax = isMaxPriority
        self.heap = Heap(None, isMaxPriority)

    def top(self):
        if self.heap.num() > 0:
            return self.heap.top()
        else:
            return None

    def removeTop(self):
        if self.heap.num() > 1:
            self.heap.data[1] = self.heap.data.pop()
            self.heap.heapify(1)
        else:
            self.heap.data = [None]

    def updateKey(self, x, k):
        if (self.isMax and k < 0) or (not self.isMax and k > 0):
            return None
        if self.heap.num() >= x > 0:
            self.heap.data[x] += k
            self.heap.heapify(x)
            self.heap.up(x)

    def add(self, x):
        self.heap.add(x)
    
