# coding: UTF-8

__all__ = [
    'UnionFind',
    'invertionPair',
    ]

class UnionFind(object):
    def __init__(self, n):
        self.indexes = np.array(range(n))

    def find(self, i):
        if self.indexes[i] != i:
            self.indexes[i] = self.find(self.indexes[i])
        return self.indexes[i]
    
    def union(self, a, b):
        r, s = self.find(a), self.find(b)
        if r < s:
            self.indexes[s] = r
        else:
            self.indexes[r] = s

    def isInSameGroup(self, a, b):
        return self.find(a) == self.find(b)
    
def inversionPair(aList):
    '''
    Find inverion pair in a list.
    That is the (i, j) pair if i < j, and A[i] > A[j].
    Return a set((i, j), ...).
    ------
    adapted to questions: [CLRS]-2-4
    '''
    class Element(object):
        def __init__(self, ele, index):
            self.ele = ele
            self.index = index

        def isLess(self, another):
            return self.ele < another.ele
        
    # augment merge sort
    eleList = [Element(ele, i) for (i, ele) in enumerate(aList)]
    def inner(eles, begin, end):
        if begin >= end:
            return set()
        mid = (begin+end)/2
        cps = inner(eles, begin, mid)
        cps.update(inner(eles, mid+1, end))
        mae, ato = eles[begin:mid+1], eles[mid+1:end+1]
        lenMae, lenAto = len(mae), len(ato)
        i, iMae, iAto = begin, 0, 0
        while iMae < lenMae and iAto < lenAto:
            if mae[iMae].isLess(ato[iAto]):
                eles[i] = mae[iMae]
                iMae += 1
                i += 1
            else:
                for j in range(iMae, lenMae):
                    cps.add((mae[j].index, ato[iAto].index))
                eles[i] = ato[iAto]
                iAto += 1
                i += 1
        while iMae < lenMae:
            eles[i] = mae[iMae]
            iMae += 1
            i += 1
        while iAto < lenAto:
            eles[i] = ato[iAto]
            iAto += 1
            i += 1
        return cps
    return inner(eleList, 0, len(eleList))
                
