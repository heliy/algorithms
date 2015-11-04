#coding: UTF-8

'''
kd-tree
'''

import numpy as np

from basicTree import BasicTree as Tree

MAXDISTANCE = 999999

def distance(item1, item2):
    return np.linalg.norm(item1-item2)

class KDTree(Tree):    
    def __init__(self, data=None, parent=None, dim=0):
        '''
        data: numpy array, shape=(n,), n is the number of node.
              every line in data should be tuple().
              last item value in one node is the classification.
              must have names in dtype.
        parent: parent node.
        dim: dimension in this node.
        '''
        self.parent = parent
        self.dim = dim
        # print data
        if data is None or data.shape[0] == 0:
            self.item = None
            self.left = None
            self.right = None
            self.cato = None
        else:
            data.sort(order=data.dtype.names[dim])
            midIndex = data.shape[0]/2
            self.item = np.array(list(data[midIndex])[:-1])
            self.cato = list(data[midIndex])[-1]
            nextDim = (dim+1)%len(self.item)
            if midIndex == 0:
                self.left = None
            else:
                self.left = KDTree(data[:midIndex], self, nextDim)
            if midIndex == data.shape[0]-1:
                self.right = None
            else:
                self.right = KDTree(data[midIndex+1:], self, nextDim)

    def isLeaf(self):
        return self.item is not None and self.left is None and self.right is None

    def findLeaf(self, item):
        if self.item == None:
            return None
        if self.isLeaf():
            return self
        if item[self.dim] <= self.item[self.dim]:
            return self.left.findLeaf(item)
        else:
            return self.right.findLeaf(item)

    def findNearest(self, item, mae=MAXDISTANCE):
        if self.item == None:
            return None
        leaf = self.findLeaf(item)
        near = None
        while leaf is not None:
            if near is None or distance(leaf.item, item) < distance(near.item, item):
                near = leaf
            leaf = leaf.parent
        return near
