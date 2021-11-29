'''
Heap data structure and common operations
'''

def heapsort(arr):
    sorted = []
    while(len(arr) > 0):
        value = extract_min(arr)
        sorted.append(value)

    return sorted

def extract_min(arr):

    min = arr[0]
    arr[0] = arr[len(arr)-1]
    arr.pop()
    heapify_down(arr, 0)    
    return min

def heap_insert(arr, value):
    arr.append(value)
    heapify_up(arr, len(arr)-1)


def heapify_up(arr, i):
    if i == 0: return
    while i > 0:
        idx_parent = get_parent(i)
        parent = arr[idx_parent]
        if parent > arr[i]:
            swap(arr, i, idx_parent)
            i = idx_parent
        else:
            break

def heapify_down(arr, i):
    while i < len(arr)-1:
        smallest = i
        lchild = get_lchild(i)
        rchild = get_rchild(i)

        if lchild < len(arr) and arr[lchild] < arr[smallest]:
            smallest = lchild
        if rchild < len(arr) and arr[rchild] < arr[smallest]:
            smallest = rchild
        
        if smallest != i:
            swap(arr, smallest, i)
            i = smallest
        else:
            break


def get_parent(i):
    return (i-1)//2

def get_lchild(i):
    return i*2+1

def get_rchild(i):
    return i*2+2

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]