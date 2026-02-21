n = int(input("Enter the number: "))
digit_sum = 0

while n > 0:
    r = n % 10
    digit_sum += r
    n = n // 10  

print("Sum of digits:", digit_sum)
