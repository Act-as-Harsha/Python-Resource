import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

# Step 1: Define dataset manually from the image
data = [
    ['High', 'Yes', 'Good', 'Yes', 'Yes'],
    ['High', 'No', 'Good', 'Yes', 'Yes'],
    ['Medium', 'Yes', 'Fair', 'No', 'Yes'],
    ['Low', 'Yes', 'Poor', 'No', 'No'],
    ['Low', 'No', 'Poor', 'No', 'No'],
    ['Medium', 'No', 'Fair', 'Yes', 'Yes'],
    ['High', 'Yes', 'Good', 'No', 'Yes'],
    ['Medium', 'Yes', 'Good', 'Yes', 'Yes'],
    ['Low', 'Yes', 'Fair', 'No', 'No'],
    ['Medium', 'No', 'Poor', 'No', 'No']
]

columns = ['Income Level', 'Employment', 'Credit Score', 'Collateral', 'Loan Approved']
df = pd.DataFrame(data, columns=columns)

# Step 2: Split into features and target
X = df.drop('Loan Approved', axis=1)
y = df['Loan Approved']

# Step 3: Encode categorical variables
encoders = {}
for column in X.columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    encoders[column] = le

# Encode target variable
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)

# Step 4: Train Naive Bayes Classifier
model = CategoricalNB()
model.fit(X, y_encoded)

# Step 5: Define input customer
input_customer = pd.DataFrame([{
    'Income Level': 'Medium',
    'Employment': 'Yes',
    'Credit Score': 'Fair',
    'Collateral': 'No'
}])

# Encode the input with same encoders
for column in input_customer.columns:
    input_customer[column] = encoders[column].transform(input_customer[column])

# Step 6: Predict probability
proba = model.predict_proba(input_customer)[0]
classes = target_encoder.inverse_transform([0, 1])

# Step 7: Display results
print("\n🔍 Probability of Loan Approval for input profile:")
for label, prob in zip(classes, proba):
    print(f"{label}: {prob:.2%}")
