'''
rotation of elements of array k positions  
'''
def k_positions_rotation(arr, k):
    result = []
    right_shift = len(arr)-k
    for i, val in enumerate(arr):
        n_rotation = right_shift + k if right_shift + k < len(arr) else (right_shift+i) % len(arr)
        result.append(arr[n_rotation])
    return result