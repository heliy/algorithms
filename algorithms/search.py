# coding: UTF-8


'''
Binary Search

search: do binary search

'''

__all__ = ['linearSearch',
           'binarySearch']

def linearSearch(list, find):
    '''
    linear Search
    return index, -1 if 404.
    -------
    adapted to questions: [CLRS]-2.1-3
    '''
    for (i, item) in enumerate(list):
        if item == find:
            return i
    return -1


def binarySearch(ordered, find):
    '''
    index = search(ordered, find)
    input:
      ordered: ascending array list (see sort.*)
      find: target item
    output:
      index: index of target item, -1 otherwise
    -----
    adapted to questions: [CLRS]-2.3-5
    '''
    low, high = 0, len(ordered)-1
    while low <= high:
        mid = (low + high)/2
        if ordered[mid] == find:
            return mid
        elif ordered[mid] < find:
            low = mid + 1
        else:
            high = mid - 1
    return -1

    
