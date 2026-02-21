a = int(input("Enter the variable a: "))
b = int(input("Enter the variable b: "))

min_num = min(a, b)

for i in range(min_num, 0, -1):
    if a % i == 0 and b % i == 0:
        hcf = i
        break

print(f"The HCF of {a} and {b} is {hcf}")
