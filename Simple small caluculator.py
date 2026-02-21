def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Select option.")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", sub(a, b))
        elif choice == '3':
            print("Result:", mul(a, b))
        elif choice == '4':
            if b == 0:
                print("Cannot divide by zero.")
            else:
                print("Result:", div(a, b))
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
