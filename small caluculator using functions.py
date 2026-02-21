def calculete(a, b): 
    total = a + b 
    diff = a - b 
    prod = a * b 
    div = a / b 
    mod = a % b
    return total, diff, prod, div, mod 

a = int(input("Enter a value: ")) 
b = int(input("Enter b value: ")) 

# Function call
s, d, p, q, m = calculete(a, b)

print("Sum = ", s)
print("Diff = ", d)
print("Mul = ", p)
print("Div = ", q)
print("Mod = ", m)
