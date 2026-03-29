# Assignment 7: Dataset Detective
# Date: 24/02/2026
# Dataset: Titanic (via seaborn)

import pandas as pd
import seaborn as sns


# -------------------------------
# Step 1: Load Dataset
# -------------------------------
df = sns.load_dataset("titanic")


# -------------------------------
# Step 2: Basic Overview
# -------------------------------
print("=" * 70)
print("        DATASET DETECTIVE — TITANIC DATASET")
print("=" * 70)

print("\n--- Top 5 Rows ---")
print(df.head().to_string(index=False))

print("\n--- Dataset Shape ---")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")


# -------------------------------
# Step 3: Numeric Column Analysis
# -------------------------------
print("\n--- Highest Value per Numeric Column ---")

numeric_cols = df.select_dtypes(include='number')

for col in numeric_cols.columns:
    print(f"{col:<20}: {df[col].max()}")


# -------------------------------
# Step 4: Missing Values Analysis
# -------------------------------
print("\n--- Missing Values per Column ---")

missing = df.isnull().sum()

for col, count in missing.items():
    if count > 0:
        pct = (count / len(df)) * 100
        print(f"{col:<20}: {count} missing ({pct:.1f}%)")


# -------------------------------
# Step 5: Insights Generation
# -------------------------------
print("\n--- Key Insights ---")

# Survival rates
overall_survival = df['survived'].mean() * 100
female_survival  = df[df['sex'] == 'female']['survived'].mean() * 100
male_survival    = df[df['sex'] == 'male']['survived'].mean() * 100

# Other stats
avg_age = df['age'].mean()
class_survival = df.groupby('pclass')['survived'].mean() * 100

print(f"1. Overall survival rate: {overall_survival:.1f}%")

print(f"2. Female survival ({female_survival:.1f}%) "
      f"is much higher than male ({male_survival:.1f}%)")

print(f"3. Average passenger age: {avg_age:.1f} years")

print(f"4. Survival by class:")
print(f"   1st Class: {class_survival[1]:.1f}%")
print(f"   2nd Class: {class_survival[2]:.1f}%")
print(f"   3rd Class: {class_survival[3]:.1f}%")

print(f"5. Columns like 'age' and 'cabin' contain high missing values.")
print("   → Require careful preprocessing before modeling.")


# -------------------------------
# Step 6: Conclusion
# -------------------------------
print("\n--- Conclusion ---")
print("The Titanic dataset reveals strong patterns in survival based on")
print("gender and passenger class. Data cleaning is essential before ML.")