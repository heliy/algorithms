#coding: UTF-8

__all__ = [
    'maxSub',
    ]

def maxSub(aList):
    '''
    Linear-time algorithm for maximum-subarray problem.
    Return (left, right, sum) of maximum subarray.
    '''
    hasPositive = False
    currentSum, maxSum = 0, 0
    maxi, maxj = 0, 0
    maxItem, maxIndex = aList[0], 0
    for (i, item) in enumerate(aList):
        if item > 0:
            hasPositive = True
        if currentSum < 0:
            currentSum = 0
            maxi, maxj = i, i
        if item > maxItem:
            maxItem, mwxIndex = item, i
        currentSum += item
        if currentSum > maxSum:
            maxj = i
            maxSum = currentSum
    if hasPositive:
        return (maxi, maxj, maxSum)
    else:
        return (maxIndex, maxIndex, maxItem)
        
