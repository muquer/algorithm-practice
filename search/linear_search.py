'''
Linear search on an array
'''
def linear_search(arr, value):
    for i, element in enumerate(arr):
        if element == value: return i
    return -1