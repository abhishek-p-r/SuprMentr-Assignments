# ==========================================
# Assignment 11: Build Your First Dataset
# Date: 03/03/2026
# ==========================================

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


# -------------------------------
# Step 1: Create Dataset
# -------------------------------

data = {
    "study_hours": [1,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11],
    "marks":       [35,42,45,50,55,58,62,65,67,70,72,75,77,80,83,85,87,90,92,95]
}

df = pd.DataFrame(data)

print("=" * 60)
print("        BUILD YOUR FIRST DATASET")
print("=" * 60)

print("\nFeature (X): study_hours  |  Label (y): marks\n")
print(df.to_string(index=False))


# -------------------------------
# Step 2: Define Features & Labels
# -------------------------------

X = df[["study_hours"]]
y = df["marks"]


# -------------------------------
# Step 3: Train Model
# -------------------------------

model = LinearRegression()
model.fit(X, y)


# -------------------------------
# Step 4: Model Details
# -------------------------------

slope = model.coef_[0]
intercept = model.intercept_
r2_score = model.score(X, y)

print("\n--- Model Details ---")
print(f"Slope     : {slope:.2f}")
print(f"Intercept : {intercept:.2f}")
print(f"R2 Score  : {r2_score:.4f}")
print(f"Formula   : marks = {slope:.2f} * hours + {intercept:.2f}")


# -------------------------------
# Step 5: Predictions
# -------------------------------

print("\n--- Predictions ---")

test_hours = [3, 6, 8, 10, 12]

for hours in test_hours:
    input_df = pd.DataFrame([[hours]], columns=["study_hours"])  # Avoid warning
    prediction = model.predict(input_df)[0]

    # Optional: cap marks at 100
    prediction = min(prediction, 100)

    print(f"Study {hours:>4} hrs  =>  Predicted Marks: {prediction:.1f}")


# -------------------------------
# Step 6: Visualization
# -------------------------------

plt.figure()

plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()
plt.grid()

plt.show()