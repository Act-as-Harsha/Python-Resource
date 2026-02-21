import math

n = float(input("Enter the n value: "))

if n <= 0:
    print("Enter a positive number.")
else:
    result = math.log(n)
    print("Natural logarithm of", n, "is", result)
