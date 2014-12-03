#Simple, but not completely brain-dead implementation of the burrow-wheelers transform.

#Instead of explicitly constructing the substrings, it constructs (and sorts) array of initial indices

LESS = -1
EQUAL = 0
GREATER = 1

def compare_substrings( data, i1, i2 ):
    """LExicographically compare 2 substrings:
    data[i1:] ++ '\0' ++ data[:i1]
    data[i2:] ++ '\0' ++ data[:i2]
    """
    if i1 == i2:
        return EQUAL
    
    n = len(data)
    
    while True:
        if i1 == n:
            return GREATER
        elif i2 == n:
            return LESS
        else:
            cc1 = data[i1]
            cc2 = data[i2]
            if cc1 < cc2:
                return LESS
            elif cc1 > cc2:
                return GREATER
            else:
                i1 += 1
                i2 += 1

def bwt(data, eof_char=None):
    indices = list(range(len(data)+1))
    qsort( indices, lambda a,b: compare_substrings(data, a,b)==LESS )

    return [ (data[i-1] if i>0 else eof_char)
             for i in indices ]

def qsort( items, less ):
    quicksort( items, 0, len(items)-1, less )

    
def quicksort(A, i, k, less=lambda x,y:x<y):
    """Code, copied and adapted from wikipedia"""
    if i < k:
        p = partition(A, i, k, less)
        quicksort(A, i, p - 1, less)
        quicksort(A, p + 1, k, less)

# left is the index of the leftmost element of the subarray
# right is the index of the rightmost element of the subarray (inclusive)
# number of elements in subarray = right-left+1
def partition(arr, left, right, less):
     #pivotIndex = choosePivot(arr, left, right)
     pivotIndex = (left+right)//2
     pivotValue = arr[pivotIndex]
     #swap arr[pivotIndex] and arr[right]
     arr[pivotIndex], arr[right] = arr[right], arr[pivotIndex]
     storeIndex = left
     for i in range(left,right):
         if less(arr[i], pivotValue):
             #swap arr[i] and arr[storeIndex]
             arr[i], arr[storeIndex] = arr[storeIndex], arr[i]
             storeIndex = storeIndex + 1
     #// Move pivot to its final place
     #swap arr[storeIndex] and arr[right]  
     arr[storeIndex], arr[right] = arr[right], arr[storeIndex]
     return storeIndex      
