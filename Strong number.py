def is_strong_number(num):
    def factorial(n):
        return 1 if n == 0 else n * factorial(n - 1)

    sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
    return sum_of_factorials == num

number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong number.")
else:
    print(f"{number} is not a Strong number.")
