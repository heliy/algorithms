# coding: UTF-8


'''
Binary Search

search: do binary search

'''

__all__ = ['search']


def search(ordered, find):
    '''
    index = search(ordered)
    input:
      ordered: ascending list (see sort.*)
      find: target item
    output:
      index: index of target item, -1 otherwise
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

    
