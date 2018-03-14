def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    #TODO your code here
    #fullname = fullname
    fullname_list = fullname.split()     # splits at each " "
    initials = "" # setting it up

    for name in fullname_list:
        initials += name[0].upper()       # gets the first letter of each name, makes it uppercase
    
    return initials

def main():
    get_name = input("What is your full name? ")
    print(get_initials(get_name))

if __name__ == "__main__":
    main()
        