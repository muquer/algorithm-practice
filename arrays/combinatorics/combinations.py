'''
Returns a list of combinations of given array
'''

def get_combinations(arr, k, i = 0, curr : list = [], combinations : list = []):
    if len(curr) < k:
        for j in range(i, len(arr)):
            curr.append(arr[j])
            get_combinations(arr, k, j+1, curr, combinations)
            curr.pop()
    elif len(curr) == k:
        combinations.append(list(curr))
        return
    return combinations