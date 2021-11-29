'''
Check if a number has more than 2 divisors
'''
def is_prime(n):
    divisor = 2
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
        divisor+=1
    
    return True