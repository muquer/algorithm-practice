'''
Returns a list of permutations of given array
'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def get_permutations(arr, i = 0, permutations : list = []):
    if i == len(arr):
        permutations.append(list(arr))
    else:
        for j in range(i, len(arr)):
            swap(arr, i, j)
            get_permutations(arr, i+1)
            swap(arr, i, j)

    return permutations