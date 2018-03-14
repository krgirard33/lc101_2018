from helpers import alphabet_position, rotate_character

# vigenere

def encrypt(mess, twist_key):
    '''encrypt an inputed text, using an inputed key'''
    e_mess = ""
    key_code = []

    # convert twist_key to key_code via forloop thru alpha_position
    for i in twist_key:
        key_code.append(alphabet_position(i))

    # forloop mess through rot_char using key_code as rot, adding it to e_mess
    key_code_pos = 0
    for i in mess:
        if i.isalpha():
            key_code_rot = key_code_pos % len(key_code)
            e_mess += rotate_character(i, key_code[key_code_rot])
            key_code_pos += 1
        else:
            e_mess += i

    # testing area
    return e_mess


def main():
    '''main, duh'''
    mess_in = input("What message would you like to encrypt? ")
    key_in = input("What key would you like encrypt it with? ")
    print(vigenere(mess_in, key_in))

if __name__ == "__main__":
    main()
    