from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    '''walks through text, sending each character to rotate_character, getting an encryted value'''
    e_mess = ""
    for i in text:
        e_mess += rotate_character(i, rot)
    return e_mess

def main():
    text_in = input("What message would you like to encrypt? ")
    rot_in = input("How far would you like to rotate it? ")
    rot = int(rot_in)
    print(encrypt(text_in, rot))

if __name__ == "__main__":
    main()
