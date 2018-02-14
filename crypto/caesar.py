from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    e_mess =""
    for i in text:
        e_mess += rotate_character(i, rot)
    return e_mess

def main():
    text_in = input("What message would you like to encrypt? ")
    rot_in = input("How far would you like to rotate it? ")
    rot = int(rot_in)
    print(encrypt(text_in, rot))
    '''print(alphabet_position("c"))
    print(alphabet_position("B"))
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
