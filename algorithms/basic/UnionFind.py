# coding: UTF-8

import numpy as np

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

    
