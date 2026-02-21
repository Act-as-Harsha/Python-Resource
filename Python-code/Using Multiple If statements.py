size = input("What size pizza do you want (S/M/L)? ")
bill = 0

if size == 'S' or size == 's':
    bill += 100
    print("Small pizza price is 100 Rs.")
elif size == 'M' or size == 'm':
    bill += 200
    print("Medium pizza price is 200 Rs.")
elif size == 'L' or size == 'l':
    bill += 300
    print("Large pizza price is 300 Rs.")
else:
    print("Invalid size selected.")
    exit()  

add_pepperoni = input("Do you want pepperoni (Y/N)? ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 30
    else:
        bill += 50

extra_cheese = input("Do you want extra cheese (Y/N)? ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 20

print(f"Your final bill is {bill} Rs.")
