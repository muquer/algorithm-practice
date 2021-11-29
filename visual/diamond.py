import math

'''
Prints a diamond pattern with length n
'''

def diamond(n):
    mid = math.ceil(n/2)
    for i in range(0, n-mid):
        blank = '-'*(n-mid-i)
        stars = ('*')*(i)
        n_str = blank + stars + '*'*(n % 2)  +  stars + blank
        print(n_str)

    for i in range(n-mid, -1, -1):
        blank = '-'*(n-mid-i)
        stars = ('*')*(i)
        n_str = blank + stars + '*'*(n % 2)  +  stars + blank
        print(n_str)