from random import *
import os
import time

u_pwd = input("Enter a password: ")
pwd = list('abcdefghijklmnopqrstuvwxyz1234567890')
pw = ""

while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw += str(guess_pwd)+str(pw)
    print("Trying password:", pw)
    time.sleep(0.1)
    os.system("cls")

print("Your password is:", pw)
