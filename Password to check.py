def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1

    if strength <= 1:
        print("😒 Weak password")
    elif strength <= 3:
        print("😏 Moderate password")
    else:
        print("👍 Strong password")

password = input("Enter your password: ")
check_password_strength(password)
