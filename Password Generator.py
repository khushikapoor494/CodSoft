# PASSWORD GENERATOR

#importing modules

import random as r
import string as s

#defining a function for creatinng a password

def  Generator(p):
    password=''      # empty string to store characters     
    charc=s.ascii_letters + s.digits + s.punctuation
    #output for above line = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    for i in range(p):   
        password+=r.choice(charc)

    return password


l=int(input("Enter the length of your password that you want to generate:"))
pas=Generator(l)
print(f'Your generated password is: {pas}')
