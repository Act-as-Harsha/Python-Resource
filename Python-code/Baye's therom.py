def bayes_theorem(prior_A, likelihood_B_given_A, marginal_B):
    return (likelihood_B_given_A * prior_A) / marginal_B

print("Enter all probabilities as decimals (e.g., 0.1 for 10%)")

prior_A = float(input("Enter P(A): "))
likelihood_B_given_A = float(input("Enter P(B|A): "))
marginal_B = float(input("Enter P(B): "))

posterior = bayes_theorem(prior_A, likelihood_B_given_A, marginal_B)

print(f"\nThe probability P(A|B) is: {posterior:.4f}")           