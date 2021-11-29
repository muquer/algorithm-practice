'''
Number that is the sum of its own digits each raised to the power of the number of digits

'''

def is_armstrong_number(n):
    
    magnitude = 0
    while (n/10**magnitude) > 1:
        magnitude+=1

    sum = 0
    digit_decomposition = n
    while digit_decomposition > 1:
        sum += (digit_decomposition % 10)**magnitude
        digit_decomposition //= 10

    return True if n == sum else False 