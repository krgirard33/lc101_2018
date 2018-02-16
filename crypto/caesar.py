<<<<<<< HEAD
def alphabet_position(letter):
    '''returns the 0-based numerical position of a letter within the alphabet varible'''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_index = -1
    letter_index = alphabet.index(letter.lower())
    return letter_index

def rotate_character(char, rot):
    ''' rotates a characater by rot number of positions'''
    char_index = -1
    encrypt_letter = -1
    base = 65   # start of upper case ord
    char_index = alphabet_position(char)
    if char.islower():
        base = 97 # start of lower case ord
        encrypt_letter = chr((char_index + rot) % 26 + base)
    elif char.isupper():
        encrypt_letter = chr((char_index + rot) % 26 + base)
    else:
        encrypt_letter = char
    """
        y = chr((ord(char)+ rot - base) % 26 + base) -- Makes it so I don't need
       alphabet_position at all. 
       """
    return encrypt_letter
=======
from helpers import alphabet_position, rotate_character
>>>>>>> 29b0d2677c830ffa5e9df576ba9b7b9fad124baa

def encrypt(text, rot):
    e_mess =""
    for i in text:
        e_mess += rotate_character(i, rot)
    return e_mess

def main():
<<<<<<< HEAD
    ''' The code in main is plainly insane '''
    char = input("Type the message you wish to encrypt: ")
    rot_in = input("Enter a number to rotate it by: ")
    rot = int(rot_in)
    print(rotate_character(char, rot))
    '''
    print(alphabet_position("c"))
    #print(alphabet_position("B"))
=======
    text_in = input("What message would you like to encrypt? ")
    rot_in = input("How far would you like to rotate it? ")
    rot = int(rot_in)
    print(encrypt(text_in, rot))
    '''print(alphabet_position("c"))
    print(alphabet_position("B"))
>>>>>>> 29b0d2677c830ffa5e9df576ba9b7b9fad124baa
    print(rotate_character("A", 1), "A 1")
    print(rotate_character("a", 1), "a 1")
    print(rotate_character("Z", 1), "Z 1")
    print(rotate_character("z", 1), "z 1")
    print(rotate_character("A", 13), "A 13")
    print(rotate_character("!", 13), "! 13")
    print(rotate_character("r", 27), "r 27")
    print(rotate_character("D", 93), "D 93")
    '''

if __name__ == "__main__":
    main()
