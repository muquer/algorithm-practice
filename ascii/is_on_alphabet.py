'''
Check whether a character is a alphabet or not
'''
def is_on_alphabet(character):
    if len(character) > 1:return False
    x=ord(character)
    True if(65<=x<=90 or 97<=x<=122) else False
