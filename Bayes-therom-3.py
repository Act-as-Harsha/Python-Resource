import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

# Step 1: Define the dataset from the image
data = [
    ['Sunny',     'Hot',  'High',   'FALSE', 'No'],
    ['Sunny',     'Hot',  'High',   'TRUE',  'No'],
    ['Overcast',  'Hot',  'High',   'FALSE', 'Yes'],
    ['Rainy',     'Mild', 'High',   'FALSE', 'Yes'],
    ['Rainy',     'Cool', 'Normal', 'FALSE', 'Yes'],
    ['Rainy',     'Cool', 'Normal', 'TRUE',  'No'],
    ['Overcast',  'Cool', 'Normal', 'TRUE',  'Yes'],
    ['Sunny',     'Mild', 'High',   'FALSE', 'No'],
    ['Sunny',     'Cool', 'Normal', 'FALSE', 'Yes'],
    ['Rainy',     'Mild', 'Normal', 'FALSE', 'Yes']
]

columns = ['Outlook', 'Temperature', 'Humidity', 'Windy', 'Play Cricket']
df = pd.DataFrame(data, columns=columns)

# Step 2: Split into features and target
X = df.drop('Play Cricket', axis=1)
y = df['Play Cricket']

# Step 3: Encode categorical variables
encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# Encode target
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)

# Step 4: Train Naive Bayes Model
model = CategoricalNB()
model.fit(X, y_encoded)

# Step 5: Define the input condition: Rainy, Cool, High, TRUE
input_data = pd.DataFrame([{
    'Outlook': 'Rainy',
    'Temperature': 'Cool',
    'Humidity': 'High',
    'Windy': 'TRUE'
}])

# Step 6: Encode input using same encoders
for col in input_data.columns:
    input_data[col] = encoders[col].transform(input_data[col])

# Step 7: Predict probabilities
proba = model.predict_proba(input_data)[0]
class_labels = target_encoder.inverse_transform([0, 1])

# Step 8: Print result
print("🔍 Probability of Playing Cricket:")
for label, prob in zip(class_labels, proba):
    print(f"➡ {label}: {prob:.2%}")
