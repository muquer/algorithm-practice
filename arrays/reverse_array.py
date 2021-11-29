'''
Reverse an array
'''

def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]

def reverse_array(arr):
    start = 0
    end = len(arr)-1

    while start < end:
        swap(arr, start, arr)
        start +=1
        end -= 1
    
    return arr