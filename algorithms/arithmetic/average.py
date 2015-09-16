# coding: UTF-8

import numpy as np

class RobbinsMonro(object):
    def __init__(self, dim):
        self.n = 0
        self.dim = dim
        self.ave = np.zeros((dim, 1))

    def getAve(self):
        return self.ave

    def getNum(self):
        return self.n

    def add(self, l):
        a = np.array(l)
        if a.shape != (dim, 1):
            raise "Unvalid input item!"+a.shape
        self.n += 1
        self.ave = self.ave + (a-self.ave)/self.n
