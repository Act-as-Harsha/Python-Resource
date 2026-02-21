# Ask user for input
print("Enter all values as percentages (like 10 for 10%)")

P_A = float(input("Enter chance of A (P(A)): ")) / 100
P_B_given_A = float(input("Enter chance of B if A is true (P(B|A)): ")) / 100
P_B = float(input("Enter overall chance of B (P(B)): ")) / 100

# Calculate Bayes' Theorem
P_A_given_B = (P_B_given_A * P_A) / P_B

# Show result as percentage
print(f"\nThe chance of A given B (P(A|B)) is: {P_A_given_B * 100:.2f}%")
