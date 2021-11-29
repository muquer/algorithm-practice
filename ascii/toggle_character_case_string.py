'''
Switch uppercase and lowercase of a string
'''
def toggle_character_case_string(input_str : str):

    l : list = list(input_str)
    
    for i in range(0,len(l)):
       
        character_code : int = ord(l[i])
        if character_code < ord('A') or character_code > ord('z'): return None
        l[i] = chr(character_code + 32 if character_code < 97 else character_code - 32)
    
    return ''.join(l)