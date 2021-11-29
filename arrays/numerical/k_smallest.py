
def k_smallest(arr : list, k):
    
    #from sort.heapsort import heapsort
    #arr = heapsort(arr)
    arr.sort()
    value = arr[k-1]
    return value
