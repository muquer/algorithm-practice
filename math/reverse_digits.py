'''
Reverse the digit order on a given number
'''

def reverse_digits(n):
    reversed_number = 0
    while n > 0:
        reversed_number = reversed_number * 10
        unit_digit = (n % 10)
        reversed_number += unit_digit
        n //= 10

    
    return reversed_number