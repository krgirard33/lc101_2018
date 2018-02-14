# helpers
def alphabet_position(letter):
    '''returns the 0-based numerical position of a letter within the alphabet variable'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_index = -1
    letter_index = alphabet.index(letter.lower())
    return letter_index

def rotate_character(char, rot):
    x = -1
    y = -1
    base = 65   # start of upper case ord
    if char.isalpha():
        x = alphabet_position(char)
        if char.islower():
            base = 97 # start of lower case ord
            y = chr((x + rot) % 26 + base)
        elif char.isupper():
            y = chr((x + rot) % 26 + base)
    else:
        y = char
    """y = chr((ord(char)+ rot - base) % 26 + base) -- Makes it so I don't need 
       alphabet_position at all. """
    return y