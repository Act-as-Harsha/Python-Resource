def find_smallest_simple(num1, num2, num3):
 
    return min(num1, num2, num3)

print("Welcome! Let's find the greatest of three numbers in a simple way.")

try:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    n3 = float(input("Enter the third number: "))
    
    smallest_number = find_smallest_simple(n1, n2, n3)

    print(f"The greatest number among them is: {smallest_number}")

except ValueError:
    print("\nInvalid input. Please enter valid numbers only.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
