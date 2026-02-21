def unique(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num
    return None
    
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

result = unique(numbers)
if result is not None:
    print("The first unique number is:", result)
else:
    print("There is no unique number.")
