def mean(n):
    n_str = str(n)
    digit_sum = sum(int(digit) for digit in n_str)
    digit_count = len(n_str)
    digit_mean = digit_sum / digit_count
    return int(digit_mean)

user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    result = mean(number)
    print("The mean of the digits is:", result)
else:
    print("Please enter a valid number.")
