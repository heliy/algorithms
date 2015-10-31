#coding: UTF-8

'''
Support Vector Machine
-----------
class perceptron
'''

import numpy as np

class perceptron(object):
    def __init__(self, n, eta):
        self.eta = eta
        self.w = np.zeros((1, n))
        self.b = 0

    def __getW(self, xs, ys, alphas):
        return sum([alphas[i]*ys[i]*xs[i] for i in range(alphas.shape[0])])
    
    def __getUn(self, xs, ys, alphas):
        w = self.__getW(xs, ys, alphas)
        for (i, x) in enumerate(xs):
            if (np.dot(w, x)+self.b)*ys[i] <= 0:
                return i
        return None
    
    def train(self, xs, ys):
        '''
        m is the amount of samples
        n is the dim of one input sample
        xs.shape = (m, n)
        ys.shape = (m,)
        '''
        alphas = np.zeros(xs.shape[0])
        while True:
            sample = self.__getUn(xs, ys, alphas)
            if sample is None:
                break
            alphas[sample] += self.eta
            self.b += self.eta*ys[sample]
        self.w = self.__getW(xs, ys, alphas)

    def test(self, x):
        return np.dot(self.w, x)+self.b


