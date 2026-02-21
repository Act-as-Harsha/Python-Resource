import random

target_password = input("Enter the password to crack: ")

keys = "0123456789abcdefghijklmnopqrstuvwxyz"

guess = ""
attempts = 0

while guess != target_password:
    guess = ""
    for i in range(len(target_password)):
        guess += random.choice(keys)
    print(f"Trying: {guess}")
    attempts += 1

print(f"Password cracked: {guess} in {attempts} attempts.")
