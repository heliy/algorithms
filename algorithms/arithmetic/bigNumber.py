#coding: UTF-8

__all__ = ['addBig']

'''
=== ATTENSION ===
the order in number list is increase.
like '3452' IS [2, 5, 4, 3], NOT [3, 4, 5, 2]
'''

def __addOne(list, num, lateral):
    list[-1] += num
    list.append(list[-1]/lateral)
    list[-2] = list[-2]%lateral

def addBig(aList, bList, lateral=2):
    '''
    add two number list into a new list.
    lateral is to set number lateral, like 16 for hex, defualt 2.
    adapted to questions: [CLRS]-2.1-4
    '''
    cList = [0]
    bLen, aLen = len(bList), len(aList)
    for (i, a) in enumerate(aList):
        if i >= bLen:
            break
        __addOne(cList, a+bList[i], lateral)
    i = min(aLen, bLen)
    while i < aLen:
        __addOne(cList, aList[i], lateral)
        i += 1
    while i < bLen:
        __addOne(cList, bList[i], lateral)
        i += 1
    if cList[-1] == 0:
        cList.pop()
    return cList
