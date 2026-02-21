import pandas as pd

# The dataset provided in the image
data = {
    'Income Level': ['High', 'High', 'Medium', 'Low', 'Low', 'Medium', 'High', 'Medium', 'Low', 'Medium'],
    'Employment': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No'],
    'Credit Score': ['Good', 'Good', 'Fair', 'Poor', 'Poor', 'Fair', 'Good', 'Good', 'Fair', 'Poor'],
    'Collateral': ['Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No'],
    'Loan Approved': ['Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No']
}
df = pd.DataFrame(data)

# Customer profile to classify
customer_profile = {
    'Income Level': 'Medium',
    'Employment': 'Yes',
    'Credit Score': 'Fair',
    'Collateral': 'No'
}

# 1. Calculate prior probabilities
total_records = len(df)
approved_count = len(df[df['Loan Approved'] == 'Yes'])
not_approved_count = len(df[df['Loan Approved'] == 'No'])

p_approved = approved_count / total_records
p_not_approved = not_approved_count / total_records

print(f"P(Approved): {p_approved}")
print(f"P(Not Approved): {p_not_approved}")
print("-" * 30)

# 2. Calculate conditional probabilities for 'Yes'
p_income_yes = len(df[(df['Loan Approved'] == 'Yes') & (df['Income Level'] == customer_profile['Income Level'])]) / approved_count
p_employment_yes = len(df[(df['Loan Approved'] == 'Yes') & (df['Employment'] == customer_profile['Employment'])]) / approved_count
p_credit_yes = len(df[(df['Loan Approved'] == 'Yes') & (df['Credit Score'] == customer_profile['Credit Score'])]) / approved_count
p_collateral_yes = len(df[(df['Loan Approved'] == 'Yes') & (df['Collateral'] == customer_profile['Collateral'])]) / approved_count

print(f"P(Income=Medium | Yes): {p_income_yes}")
print(f"P(Employment=Yes | Yes): {p_employment_yes}")
print(f"P(Credit=Fair | Yes): {p_credit_yes}")
print(f"P(Collateral=No | Yes): {p_collateral_yes}")
print("-" * 30)

# 3. Calculate conditional probabilities for 'No'
p_income_no = len(df[(df['Loan Approved'] == 'No') & (df['Income Level'] == customer_profile['Income Level'])]) / not_approved_count
p_employment_no = len(df[(df['Loan Approved'] == 'No') & (df['Employment'] == customer_profile['Employment'])]) / not_approved_count
p_credit_no = len(df[(df['Loan Approved'] == 'No') & (df['Credit Score'] == customer_profile['Credit Score'])]) / not_approved_count
p_collateral_no = len(df[(df['Loan Approved'] == 'No') & (df['Collateral'] == customer_profile['Collateral'])]) / not_approved_count

print(f"P(Income=Medium | No): {p_income_no}")
print(f"P(Employment=Yes | No): {p_employment_no}")
print(f"P(Credit=Fair | No): {p_credit_no}")
print(f"P(Collateral=No | No): {p_collateral_no}")
print("-" * 30)

# 4. Compute unnormalized probabilities
prob_yes = p_approved * p_income_yes * p_employment_yes * p_credit_yes * p_collateral_yes
prob_no = p_not_approved * p_income_no * p_employment_no * p_credit_no * p_collateral_no

print(f"Unnormalized P(Yes | Profile): {prob_yes}")
print(f"Unnormalized P(No | Profile): {prob_no}")
print("-" * 30)

# 5. Normalize and find final probability of approval
total_prob = prob_yes + prob_no
final_p_approved = prob_yes / total_prob

print(f"Final probability of Loan Approval: {final_p_approved:.4f}")

if prob_yes > prob_no:
    print("\nBased on the Naïve Bayes classifier, the loan is likely to be Approved.")
else:
    print("\nBased on the Naïve Bayes classifier, the loan is likely to be Not Approved.")
