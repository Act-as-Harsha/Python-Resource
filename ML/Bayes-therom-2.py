import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

# Step 1: Define the dataset from the image
data = [
    ['Low',    'Low',    'Poor',    'No',  'Fail'],
    ['Low',    'Medium', 'Average', 'No',  'Fail'],
    ['High',   'Low',    'Good',    'Yes', 'Pass'],
    ['Medium', 'Medium', 'Good',    'Yes', 'Pass'],
    ['High',   'High',   'Good',    'Yes', 'Pass'],
    ['Medium', 'Low',    'Average', 'No',  'Fail'],
    ['High',   'Medium', 'Good',    'No',  'Pass'],
    ['Low',    'High',   'Poor',    'No',  'Fail'],
    ['Medium', 'Medium', 'Good',    'Yes', 'Pass'],
    ['High',   'Medium', 'Average', 'Yes', 'Pass']
]

columns = ['Study Hours', 'Sleep Hours', 'Attendance', 'Notes Prepared', 'Result']
df = pd.DataFrame(data, columns=columns)

# Step 2: Split into features and label
X = df.drop('Result', axis=1)
y = df['Result']

# Step 3: Encode categorical features
encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

# Encode the target column
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Step 4: Train the Naive Bayes model
model = CategoricalNB()
model.fit(X, y_encoded)

# Step 5: Define the input student profile
# Profile: Study Hours = Medium, Sleep Hours = Low, Attendance = Good, Notes = Yes
input_data = pd.DataFrame([{
    'Study Hours': 'Medium',
    'Sleep Hours': 'Low',
    'Attendance': 'Good',
    'Notes Prepared': 'Yes'
}])

# Encode input using the same encoders
for col in input_data.columns:
    input_data[col] = encoders[col].transform(input_data[col])

# Step 6: Predict probability
proba = model.predict_proba(input_data)[0]
class_names = label_encoder.inverse_transform([0, 1])  # 0 = Fail, 1 = Pass

# Step 7: Display probabilities
print("🔍 Probability the student will:")
for label, prob in zip(class_names, proba):
    print(f"➡ {label}: {prob:.2%}")
