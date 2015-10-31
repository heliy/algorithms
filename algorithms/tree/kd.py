#coding: UTF-8

'''
kd-tree
'''

class kdTree(object):
    def __init__(self, parent):
        self.left = None
        self.right = None
        self.cato = None
        self.parent = parent

    def add(self, xs, ys, dim=0):
        if xs is None or len(xs) == 0:
            return
        
