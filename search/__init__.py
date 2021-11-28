import sys
from search.binary_search_shifted import binary_search_shifted
from search.binary_search import binary_search 
from search.linear_search import linear_search 


# Driver Code
arr = [1, 2, 3, 4, 7, 9, 10, 40]
value = 10

class Search:
    def __call__(self):

        # linear search call
        result = linear_search(arr,value)
        
        if result != -1:
            print("Linear Search : Element is present at index % d" % result)
        else:
            print("Linear Search : Element is not present in array")
        
        # binary search call
        result = binary_search(arr, value, 0, len(arr)-1)
        
        if result != -1:
            print("Binary Search : Element is present at index % d" % result)
        else:
            print("Binary Search : Element is not present in array")


        # shifted binary search call
        result = binary_search_shifted(arr, value, 0, len(arr)-1)
        
        if result != -1:
            print("Shifted Binary Search : Element is present at index % d" % result)
        else:
            print("Shifted Binary Search : Element is not present in array")


sys.modules[__name__] = Search()