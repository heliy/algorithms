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
        if index <= 0:
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

    def build(self):
        for i in range(self.num()//2, 0, -1):
            self.heapify(i)
        
        
