'''
Longest palindrome in an array

'''

def window_slide(arr, i, j):
    while True:
        if i >= 0 and j < len(arr) and arr[i] == arr[j]:
            i -= 1
            j += 1
        else:
            i += 1
            j -= 1
            break
    return len(arr[i:j+1])


def longest_palindrome_size_in_array(arr):
    palindromes = []
    for i in range(0, len(arr)):
        
        maxx = max(window_slide(arr, i, i+1), window_slide(arr, i, i))
        palindromes.append(maxx)      
        
    
    return max(palindromes)