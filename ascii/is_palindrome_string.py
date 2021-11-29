'''
Check if the given string is Palindrome
'''

def is_palindrome_string(value: str):
    #return True if value == value[::-1] else False
    for i in range(0, len(value)//2):
        if value[i] != value[len(value)-1-i]:
            return False

    return True
    