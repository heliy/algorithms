#coding: UTF-8

__all__ = [
    'bubbleSort',
    'insertionSorted',
    'insertionSort_recu',
    'selectionSort',
    'mergeSort',
    'heapSort',
    'quickSort',
]

from random import randint
    
from heap import Heap
from utils import isLessThan, isMoreThan

def bubbleSort(aList, increaseOrder=True):
    '''
    inplace version of bubble sort algorithm.
    return NOTHING.
    -----
    adapted to questions: [CLRS]-2-2
    '''
    func = increaseOrder and isLessThan or isMoreThan
    for i in range(len(aList)):
        for j in range(i):
            if func(aList[i], aList[j]):
                aList[i], aList[j] = aList[j], aList[i]

def insertionSorted(aList, increaseOrder=True):
    '''
    non-recursive version of insertion sort algorithm
    return a sorted list
    -----
    refer to [CLRS]-2.1
    adapted to questions: [CLRS]-2.1-2
    '''
    sorted = [None]*len(aList)
    sorted[0] = aList[0]
    f = increaseOrder and isLessThan or isMoreThan    
    for (i, item) in enumerate(aList[1:]):
        # begin 0 in the second, so we need not minus one...
        while i >= 0 and f(item, sorted[i]):
            sorted[i+1] = sorted[i]
            i -= 1
        sorted[i+1] = item
    return sorted

def insertedSort_recu(aList, increaseOrder=True):
    '''
    recursive version of inplace inserttion selection algorithm.
    return NOTHING.
    -----
    adapted to questions: [CLRS]-2.3-5
    '''
    def __insertedSort_recu(aList, end, func):
        if end <= 0:
            return
        __insertedSort_recu(aList, end-1, func)
        thisItem = aList[end]
        i = end-1
        while i >= 0 and func(thisItem, aList[i]):
            aList[i+1] = aList[i]
            i -= 1
        aList[i+1] = thisItem
    func = increaseOrder and isLessThan or isMoreThan
    __insertedSort_recu(aList, len(aList)-1, func)

def selectionSort(aList, increaseOrder=True):
    '''
    inplace version of selection sort.
    return NOTHING.
    -----
    adapted to questions: [CLRS]-2.2-2
    '''
    func = increaseOrder and min or max
    for i in range(len(aList)):
        minValue = func(aList[i:])
        index = aList.index(minValue)
        aList[i], aList[index] = aList[index], aList[i]
    
def mergeSort(aList, increaseOrder=True):
    '''
    inplace version of merge sort.
    return NOTHING.
    -----
    refer to [CLRS]-2.3.1
    '''    
    def __mergeSort(aList, p, r, f):
        if p >= r:
            return
        mid = (p+r)/2
        __mergeSort(aList, p, mid, increaseOrder)
        __mergeSort(aList, mid+1, r, increaseOrder)
        mae, ato = aList[p:mid+1], aList[mid+1:r+1]
        lenMae, lenAto = len(mae), len(ato)
        i, iMae, iAto = p, 0, 0
        while iMae < lenMae and iAto < lenAto:
            if f(mae[iMae], ato[iAto]):
                aList[i] = mae[iMae]
                iMae += 1
            else:
                aList[i] = ato[iAto]
                iAto += 1
            i += 1
        while iMae < lenMae:
            aList[i] = mae[iMae]
            i += 1
            iMae += 1
        while iAto < lenAto:
            aList[i] = ato[iAto]
            i += 1
            iAto += 1
    f = increaseOrder and isLessThan or isMoreThan
    __mergeSort(aList, 0, len(aList)-1, f)

def heapSort(aList, increaseOrder=True):
    '''
    heap sort.
    heap is implemanted in heap.Heap
    return List.
    ------
    refer to [CLRS]-6.4
    '''
    heap = Heap(aList, not increaseOrder)
    newList = []
    for i in range(heap.num(), 1, -1):
        heap.data[1], heap.data[i] = heap.data[i], heap.data[1]
        newList.append(heap.data.pop())
        heap.heapify(1)
    newList.append(heap.top())
    return newList

def quickSort(aList, increaseOrder=True):
    '''
    inplace randomized quick sort.
    return NOTHING.
    ------
    refer to [CLRS]-7.1, 7.3
    '''
    f = increaseOrder and isLessThan or isMoreThan
    def __qsort(aList, p, r):
        i = randint(p, r)
        aList[i], aList[r] = aList[r], aList[i]
        if p < r:
            x = aList[r]
            q = p - 1
            for j in range(p, r):
                if f(aList[j], x):
                    q += 1
                    aList[q], aList[j] = aList[j], aList[q]
            q += 1
            aList[q], aList[r] = aList[r], aList[q]
            __qsort(aList, p, q-1)
            __qsort(aList, q+1, r)
    __qsort(aList, 0, len(aList)-1)
