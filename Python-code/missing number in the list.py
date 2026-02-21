def find_missing_number(numbers):
    n = len(numbers) + 1  
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number

numbers = [1, 2, 4, 5, 6]  
print("Missing number is:", find_missing_number(numbers))
