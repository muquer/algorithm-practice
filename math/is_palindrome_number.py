'''
Check if the reverse of a number and original number both are equal
'''

from reverse_digits import *
def is_palindrome_number(n):
    reversed_n = reverse_digits(n)
    return True if n*reversed_n >= 0 and n == reversed_n else False

