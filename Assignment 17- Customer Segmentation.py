# ==========================================
# Assignment 17: Customer Segmentation (K-Means)
# Date: 18/03/2026
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# -------------------------------
# Step 1: Generate Dataset
# -------------------------------

def create_dataset():
    np.random.seed(42)

    ages = np.concatenate([
        np.random.normal(25, 4, 40),
        np.random.normal(35, 5, 50),
        np.random.normal(45, 5, 50),
        np.random.normal(55, 6, 30),
        np.random.normal(30, 4, 30)
    ])

    income = np.concatenate([
        np.random.normal(25, 5, 40),
        np.random.normal(70, 8, 50),
        np.random.normal(55, 8, 50),
        np.random.normal(40, 7, 30),
        np.random.normal(85, 7, 30)
    ])

    spending = np.concatenate([
        np.random.normal(75, 8, 40),
        np.random.normal(70, 8, 50),
        np.random.normal(45, 8, 50),
        np.random.normal(30, 7, 30),
        np.random.normal(80, 7, 30)
    ])

    df = pd.DataFrame({
        "Age": ages,
        "Annual_Income": income,
        "Spending_Score": spending
    }).clip(lower=0)

    return df


# -------------------------------
# Step 2: Scale Features
# -------------------------------

def scale_features(df):
    X = df[["Annual_Income", "Spending_Score"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X, X_scaled, scaler


# -------------------------------
# Step 3: Elbow Method
# -------------------------------

def compute_elbow(X_scaled):
    inertia = []

    for k in range(1, 11):
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        model.fit(X_scaled)
        inertia.append(model.inertia_)

    return inertia


# -------------------------------
# Step 4: Apply K-Means
# -------------------------------

def apply_kmeans(X_scaled, k=5):
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    return model, labels


# -------------------------------
# Step 5: Cluster Summary
# -------------------------------

def get_summary(df):
    summary = df.groupby("Cluster")[["Annual_Income", "Spending_Score"]].mean().round(1)
    return summary


# -------------------------------
# Step 6: Visualization
# -------------------------------

def plot_results(df, model, scaler, inertia):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # ---- Plot 1: Clusters ----
    ax1 = axes[0]

    for cluster_id in sorted(df["Cluster"].unique()):
        cluster_data = df[df["Cluster"] == cluster_id]

        ax1.scatter(
            cluster_data["Annual_Income"],
            cluster_data["Spending_Score"],
            label=f"Cluster {cluster_id + 1}",
            alpha=0.8
        )

    # Plot centroids
    centers = scaler.inverse_transform(model.cluster_centers_)
    ax1.scatter(
        centers[:, 0],
        centers[:, 1],
        marker='X',
        s=180,
        label="Centroids"
    )

    ax1.set_title("Customer Segmentation (K=5)")
    ax1.set_xlabel("Annual Income (k$)")
    ax1.set_ylabel("Spending Score")
    ax1.legend()
    ax1.grid()

    # ---- Plot 2: Elbow Method ----
    ax2 = axes[1]

    ax2.plot(range(1, 11), inertia, marker='o')
    ax2.axvline(x=5, linestyle='--', label="Optimal K=5")

    ax2.set_title("Elbow Method")
    ax2.set_xlabel("Number of Clusters (K)")
    ax2.set_ylabel("Inertia (WCSS)")
    ax2.legend()
    ax2.grid()

    plt.tight_layout()

    # Save figure
    plt.savefig("kmeans_clusters.png", dpi=150)
    print("\n[Plot saved as 'kmeans_clusters.png']")

    plt.show()


# -------------------------------
# Main Function
# -------------------------------

def main():
    print("=== Customer Segmentation (K-Means) ===\n")

    # Dataset
    df = create_dataset()
    print("Dataset Preview:")
    print(df.head())

    # Scaling
    X, X_scaled, scaler = scale_features(df)

    # Elbow
    inertia = compute_elbow(X_scaled)

    # KMeans
    model, labels = apply_kmeans(X_scaled, k=5)
    df["Cluster"] = labels

    # Summary
    print("\n=== Cluster Summary ===")
    summary = get_summary(df)
    print(summary)

    # Visualization
    plot_results(df, model, scaler, inertia)


# Entry Point
if __name__ == "__main__":
    main()