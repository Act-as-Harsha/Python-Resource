def biggest(a, b): 
    if a > b:
        return a 
    else:
        return b

a = int(input("Enter a value: ")) 
b = int(input("Enter b value: ")) 

big = biggest(a, b) 
print("Big number = ", big)
