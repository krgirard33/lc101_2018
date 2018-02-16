
def alphabet_position(letter):
    '''returns the 0-based numerical position of a letter within the alphabet variable'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_index = -1
    letter_index = alphabet.index(letter.lower())
    return letter_index

def rotate_character(char, rot):
    '''moves char rot number of spaces further down the alpabet'''
    temp_pos = -1
    new_letter = -1
    base = 65   # start of upper case ord
    if char.isalpha():
        temp_pos = alphabet_position(char)
        if char.islower():
            base = 97 # start of lower case ord
            new_letter = chr((temp_pos + rot) % 26 + base)
        elif char.isupper():
            new_letter = chr((temp_pos + rot) % 26 + base)
    else:
        new_letter = char
    """y = chr((ord(char)+ rot - base) % 26 + base) -- Makes it so I don't need 
       alphabet_position at all."""
    return new_letter

def main():
    '''main, duh'''
    print(rotate_character("a", 1))

if __name__ == "__main__":
    main()
