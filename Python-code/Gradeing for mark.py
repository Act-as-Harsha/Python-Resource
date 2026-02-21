m1 = float(input("Enter the marks you gained: "))

if m1 < 50:
    print("You got a grade F")
elif 50 <= m1 < 60:
    print("You got a grade D")
elif 60 <= m1 < 70:
    print("You got a grade C")
elif 70 <= m1 < 80:
    print("You got a grade B")
elif 80 <= m1 < 90:
    print("You got a grade A")
elif 90 <= m1 <= 100:
    print("You got a grade Excellent")
else:
    print("Invalid marks entered. Please enter a number between 0 and 100.")
