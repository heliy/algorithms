#coding: UTF-8

__all__ = [
    'hornerGenerator',
    ]

def hornerGenerator(paList):
    '''
    Horer's rule for evaluating a polynomial.
    return a evaluational function.
    ------
    useage:
       # function to evalutate 1*x^0+2*x^1+3*x^2
       func = hornerGenerator([1, 2, 3])   
       y = func(2)                        # y = 17
    -------
    adapted to questions: [CLRS]-2-3
    '''
    def horner(x):
        y = 0        
        for i in paList[::-1]:
            y = i + x*y
        return y
    return horner
