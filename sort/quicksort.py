'''
Quicksort sorting algorithm 
'''

def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]

def part(arr, start, end):
    pivot = arr[end]
    pivot_index = end
    while start < end:
        while arr[start] < pivot and start < len(arr)-1:
            start += 1

        while arr[end] > pivot and end > 0:
            end -=1
        
        if start < end:
            swap(arr, start, end)
    swap(arr, pivot_index, end)
    return end

def quicksort(arr, start, end):
    if start == end or start > end: return
    p = part(arr, start, end)
    quicksort(arr, start, p-1)
    quicksort(arr, p+1, end)



    