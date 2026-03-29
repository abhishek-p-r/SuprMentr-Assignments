# ==========================================
# Assignment 8: Data Doctor - Data Cleaning
# Date: 26/02/2026
# ==========================================

import pandas as pd
import numpy as np


# -------------------------------
# Create Dataset
# -------------------------------

data = {
    "name":   ["Alice", "bob", "CHARLIE", "Diana", "Alice", "eve", None, "Frank"],
    "age":    [25, None, 30, 22, 25, 28, 35, None],
    "city":   ["Mumbai", "delhi", "MUMBAI", "Pune", "Mumbai", "Delhi", "pune", "Bangalore"],
    "salary": [50000, 45000, None, 38000, 50000, 42000, 60000, 55000],
    "email":  [
        "alice@mail.com", "bob@mail.com", "charlie@mail.com", "diana@mail.com",
        "alice@mail.com", "eve@mail.com", "temp@mail.com", None
    ]
}

df = pd.DataFrame(data)


# -------------------------------
# BEFORE CLEANING
# -------------------------------

print("=" * 60)
print("            BEFORE CLEANING")
print("=" * 60)

print(df.to_string())

print(f"\nShape: {df.shape}")

print("\nMissing Values:")
print(df.isnull().sum())

print(f"\nDuplicate Rows: {df.duplicated().sum()}")


# -------------------------------
# DATA CLEANING STEPS
# -------------------------------

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Fill missing values
df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].mean())

# 3. Drop rows with missing critical values
df = df.dropna(subset=["name", "email"])

# 4. Standardize text formatting
df["name"] = df["name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()

# 5. Reset index
df = df.reset_index(drop=True)


# -------------------------------
# AFTER CLEANING
# -------------------------------

print("\n" + "=" * 60)
print("             AFTER CLEANING")
print("=" * 60)

print(df.to_string())

print(f"\nFinal Shape: {df.shape}")
print(f"Missing Values Left: {df.isnull().sum().sum()}")


# -------------------------------
# OBSERVATIONS
# -------------------------------

print("\n--- Why Data Cleaning Matters ---")

print("1. Machine learning models cannot handle missing values (NaN).")
print("2. Duplicate records distort analysis and create bias.")
print("3. Inconsistent text leads to incorrect grouping of categories.")
print("4. Clean data improves accuracy and reliability of predictions.")