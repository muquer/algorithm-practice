import math

'''
Prints a pyramid pattern with length n
'''
def pyramid(n):
    mid = math.ceil(n/2)
    for i in range(0, n-mid):
        blank = '-'*(n-mid-i)
        stars = ('*')*(i)
        n_str = blank + stars + '*'*(n % 2)  +  stars + blank
        print(n_str)
        