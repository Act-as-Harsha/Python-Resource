a = int(input("Enter the number: "))

fact = 1  
if a < 0:
    print("Factorial doesn't exist for negative numbers.")
elif a == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, a + 1):
        fact *= i  
    print(f"Factorial of {a} is {fact}")
