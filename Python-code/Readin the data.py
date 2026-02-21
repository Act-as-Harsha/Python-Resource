# -------------------- IMPORT LIBRARIES --------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -------------------- LOAD DATASET --------------------
# Make sure csn_klef.xlsx is in the SAME folder as this file
df = pd.read_excel("E:\Machine-learning-with-python\Machine learning with python\csn_klef.xlsx")

print("Dataset Preview:")
print(df.head())

# -------------------- EXTRACT COLUMN --------------------
data = df["Average_RF"]

# -------------------- DESCRIPTIVE STATISTICS --------------------
total_sum = data.sum()
mean = data.mean()
median = data.median()
mode = data.mode().values
std_dev = data.std()
cv = (std_dev / mean) * 100

# -------------------- PRINT RESULTS --------------------
print("\nStatistical Measures:")
print("Sum:", total_sum)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", std_dev)
print("Coefficient of Variation (%):", cv)

# -------------------- PREPARE DATA FOR PLOTS --------------------
y_rf = df["Average_RF"].values
y_rfday = df["Average_RFDAY"].values
x_labels = df["Decades"]

# -------------------- LINE GRAPH --------------------
plt.figure(figsize=(10, 4))

plt.plot(x_labels, y_rf, color='red', marker='o',
         linewidth=2, label='Average_RF')

plt.plot(x_labels, y_rfday, color='blue', marker='s',
         linewidth=2, label='Average_RFDAY')

plt.xlabel("Decades", fontsize=14, fontweight='bold')
plt.ylabel("Values", fontsize=14, fontweight='bold')
plt.title("Average Rainfall and Rainy Days by Decades",
          fontsize=16, fontweight='bold')
plt.legend()
plt.grid(True)
plt.show()

# -------------------- PIE CHART --------------------
plt.figure(figsize=(8, 8))

plt.pie(
    y_rf,
    labels=x_labels,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 12, 'fontweight': 'bold'}
)

plt.title("Average Rainfall Distribution by Decades",
          fontsize=16, fontweight='bold')

plt.axis('equal')   # ensures perfect circle
plt.show()
# -------------------- BAR GRAPH --------------------
plt.figure(figsize=(10, 4))
plt.bar(x_labels, y_rf, width=0.6, color='blue')

plt.xlabel("Decades", fontsize=18, fontweight='bold')
plt.ylabel("Average Rainfall(mm)", fontsize=18, fontweight='bold')
plt.title("Average Rainfall by Decades (Bar Graph)", fontsize=18, fontweight='bold')
plt.grid(axis='y')
plt.show()