a = int(input("Enter the variable a: "))
b = int(input("Enter the variable b: "))

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        lcm = max_num
        break
    max_num += 1

print(f"The LCM of {a} and {b} is {lcm}")
