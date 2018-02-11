def alphabet_position(letter):
    '''returns the 0-based numerical position of a letter within the alphabet varible'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_index = -1
    letter_index = alphabet.index(letter.lower())
    return letter_index

def rotate_character(char, rot):
    x = -1
    y = -1
    base = 65   # start of upper case ord
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


def main():
    #print(alphabet_position("c"))
    #print(alphabet_position("B"))
    print(rotate_character("A", 1), "A 1")
    print(rotate_character("a", 1), "a 1")
    print(rotate_character("Z", 1), "Z 1")
    print(rotate_character("z", 1), "z 1")
    print(rotate_character("A", 13), "A 13")
    print(rotate_character("!", 13), "! 13")
    print(rotate_character("r", 27), "r 27")
    print(rotate_character("D", 93), "D 93")

if __name__ == "__main__":
    main()