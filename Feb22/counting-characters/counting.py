'''
Write a program that calculates the number of times each character 
occurs in a string and prints these stats to the console. You could get 
the string as input from the user, but for the sake of simplicity, 
you may also hard-code the string into your program as the value of 
a variable. Here’s a test string, for your convenience:
'''
import pprint

def counting(test_string):
    counted = {}
    for char in test_string:  # look up if counted.get(char,False)
        if char in counted:
            counted[char] = counted[char]+ 1
        else:
            counted[char]= 1
    
    for key in counted:
        print(key, counted[key])

    pprint.pprint(counted)



def main():
    test_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus.'
    counting(test_string)

if __name__ == '__main__':
    main()
