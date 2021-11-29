'''
Convert from given base to decimal
'''

def convert_to_decimal(n, base):
    sum = 0
    i = 0
    while n > 0:
        digit = (n % 10)*(base**i)
        sum += digit
        i += 1
        n //= 10
    
    return sum