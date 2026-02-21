def is_palindrome(word):
    if word == word[::-1]:
        print(f"The word '{word}' is a palindrome.")
    else:
        print(f"The word '{word}' is not a palindrome.")

# Get input from the user
user_input = input("Enter a word: ")
is_palindrome(user_input)
