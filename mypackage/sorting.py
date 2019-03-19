def bubble_sort(items):
    '''
    Return array of items, sorted in ascending order

    Args:
        items (list): items that must be sorted.
    Returns:
        array: Return array of items, sorted in ascending order.

    Examples:
        >>> bubble_sort([3,6,2,78])
        [2,3,6,78]
        >>> bubble_sort(['r','a','f'])
        ['a','f','r']
    '''
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items

def merge_sort(alist):
    '''
    Return array of items, sorted in ascending order

    Args:
        items (list): items that must be sorted.
    Returns:
        array: Return array of items, sorted in ascending order.

    Examples:
        >>> merge_sort([3,6,2,78])
        [2,3,6,78]
        >>> merge_sort(['r','a','f'])
        ['a','f','r']
    '''

    if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       merge_sort(lefthalf)
       merge_sort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1
    return alist

def quick_sort(alist):
    '''
    Return array of items, sorted in ascending order

    Args:
        items (list): items that must be sorted.
    Returns:
        array: Return array of items, sorted in ascending order.

    Examples:
        >>> quick_sort([3,6,2,78])
        [2,3,6,78]
        >>> quick_sort(['r','a','f'])
        ['a','f','r']
    '''

    def quickSortHelper(alist,first,last):
       if first<last:

           splitpoint = partition(alist,first,last)

           quickSortHelper(alist,first,splitpoint-1)
           quickSortHelper(alist,splitpoint+1,last)


    def partition(alist,first,last):
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:
           while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1
           while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
               rightmark = rightmark -1
           if rightmark < leftmark:
               done = True
           else:
               temp = alist[leftmark]
               alist[leftmark] = alist[rightmark]
               alist[rightmark] = temp
    
       temp = alist[first]
       alist[first] = alist[rightmark]
       alist[rightmark] = temp
       return rightmark

    quickSortHelper(alist,0,len(alist)-1)
    return alist
