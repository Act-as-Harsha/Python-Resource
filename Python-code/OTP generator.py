import random


otp = random.randint(100000, 999999)
print("Your OTP is", otp)


entered_otp = int(input("Enter the OTP: "))


if entered_otp == otp:
    print("OTP verified successfully!")
else:
    print("Invalid OTP. Please try again.")
