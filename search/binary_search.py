def binary_search(arr, value, start, end):
    
    if start > end: return -1
    
    mid = start + (end - start)//2
    
    if value == arr[mid]: return mid
    
    if value < arr[mid]:
        return binary_search(arr, value, start, mid-1)
    
    if value > arr[mid]:
        return binary_search(arr, value, mid+1, end)
