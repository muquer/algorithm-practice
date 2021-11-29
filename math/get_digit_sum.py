'''
Get the sum of individual digits
'''
def get_digit_sum(n):
    sum = 0
    while n > 1:
        sum += (n % 10)
        n /= 10

    return sum