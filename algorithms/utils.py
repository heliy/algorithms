# coding: UTF-8

isLessThan = lambda x, y: x < y
isMoreThan = lambda x, y: x > y


def getElemMap(list):
    '''
    get a map of elements and index from a list.
    '''
    d = {}
    for (i, item) in enumerate(list):
        if item in d:
            d[item] = [i]
        else:
            d[item].append(i)
    return d
