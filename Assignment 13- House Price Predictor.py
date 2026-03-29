# ==========================================
# Assignment 13: House Price Predictor
# Date: 09/03/2026
# ==========================================

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


# -------------------------------
# Step 1: Create Dataset
# -------------------------------

def create_dataset(n: int = 100) -> pd.DataFrame:
    np.random.seed(42)

    area = np.random.randint(500, 3000, n)
    bedrooms = np.random.randint(1, 6, n)
    age = np.random.randint(0, 30, n)

    price = (area * 0.05) + (bedrooms * 3) - (age * 0.5) + np.random.normal(0, 5, n)
    price = np.round(price, 2)

    return pd.DataFrame({
        "area": area,
        "bedrooms": bedrooms,
        "age": age,
        "price": price
    })


# -------------------------------
# Step 2: Train Model
# -------------------------------

def train_model(df: pd.DataFrame):
    X = df[["area", "bedrooms", "age"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, X_test, y_test, X.columns


# -------------------------------
# Step 3: Evaluate Model
# -------------------------------

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\n--- Model Performance ---")
    print(f"R2 Score : {r2:.4f}")
    print(f"RMSE     : {np.sqrt(mse):.2f} lakhs")

    return y_pred


# -------------------------------
# Step 4: Display Coefficients
# -------------------------------

def display_coefficients(model, feature_names):
    print("\n--- Model Coefficients ---")

    for feature, coef in zip(feature_names, model.coef_):
        print(f"{feature:<12}: {coef:.4f}")

    print(f"Intercept   : {model.intercept_:.4f}")


# -------------------------------
# Step 5: Predict New Data
# -------------------------------

def predict_new_houses(model):
    print("\n--- Predict New Houses ---")

    new_houses = pd.DataFrame({
        "area": [1200, 2000, 800],
        "bedrooms": [2, 4, 1],
        "age": [5, 10, 20]
    })

    predictions = model.predict(new_houses)

    for i, row in new_houses.iterrows():
        print(
            f"Area={row['area']} sqft, "
            f"{row['bedrooms']} BHK, "
            f"{row['age']} yrs old "
            f"=> Price: {predictions[i]:.2f} Lakhs"
        )


# -------------------------------
# Main Function
# -------------------------------

def main():
    print("=== House Price Predictor ===\n")

    df = create_dataset()

    print("Dataset Sample (first 5 rows):")
    print(df.head().to_string(index=False))

    model, X_test, y_test, feature_names = train_model(df)

    evaluate_model(model, X_test, y_test)
    display_coefficients(model, feature_names)
    predict_new_houses(model)


# Entry Point
if __name__ == "__main__":
    main()