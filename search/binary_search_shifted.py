'''
Binary search on an ordered array with offset
'''

def binary_search_shifted(arr, value, start, end):
    
    if start > end: return -1

    mid = start + (end - start)//2

    if arr[mid] == value: return mid
    
    
    if arr[start] < arr[end]:
        if value < arr[mid]:
            return binary_search_shifted(arr, value, start, mid-1)
        elif value > arr[mid]:
            return binary_search_shifted(arr, value, mid+1, end)
    elif arr[start] > arr[end]:
        if value < arr[mid]:
            return binary_search_shifted(arr, value, mid+1, end)
        elif value > arr[mid]:
            return binary_search_shifted(arr, value, start, mid-1)
