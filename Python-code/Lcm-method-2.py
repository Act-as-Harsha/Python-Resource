import math

a = int(input("Enter the variable a: "))
b = int(input("Enter the variable b: "))

lcm = abs(a * b) // math.gcd(a, b)

print(f"The LCM of {a} and {b} is {lcm}")
