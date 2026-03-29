# ==========================================
# Assignment 15: Customer Segmentation with K-Means
# Date: 11/03/2026
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# -------------------------------
# Step 1: Generate Dataset
# -------------------------------

def generate_data(n=200):
    np.random.seed(42)

    income = np.concatenate([
        np.random.normal(30, 8, 40),
        np.random.normal(55, 8, 60),
        np.random.normal(80, 8, 50),
        np.random.normal(40, 5, 30),
        np.random.normal(90, 7, 20),
    ])[:n]

    spending = np.concatenate([
        np.random.normal(70, 10, 40),
        np.random.normal(50, 12, 60),
        np.random.normal(80, 8, 50),
        np.random.normal(20, 8, 30),
        np.random.normal(30, 10, 20),
    ])[:n]

    income = np.clip(income, 10, 120)
    spending = np.clip(spending, 5, 100)

    df = pd.DataFrame({
        "annual_income_k": income.round(1),
        "spending_score": spending.round(1)
    })

    return df


# -------------------------------
# Step 2: Scale Data
# -------------------------------

def scale_features(df):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    return scaled_data, scaler


# -------------------------------
# Step 3: Apply K-Means
# -------------------------------

def perform_clustering(data, k=5):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(data)
    return kmeans, labels


# -------------------------------
# Step 4: Cluster Summary
# -------------------------------

def cluster_summary(df):
    summary = df.groupby("cluster").agg(
        Count=("cluster", "count"),
        Avg_Income=("annual_income_k", "mean"),
        Avg_Spending=("spending_score", "mean")
    ).round(1)

    return summary


# -------------------------------
# Step 5: Business Strategy
# -------------------------------

def print_strategies(summary):
    print("\n--- Business Strategies ---\n")

    strategies = {
        0: "Impulsive Buyers → Flash sales, limited-time offers",
        1: "Mainstream Customers → Regular promotions",
        2: "VIP Customers → Premium services & exclusive products",
        3: "Budget Customers → Discounts & affordable products",
        4: "Saver Customers → Value bundles & long-term benefits"
    }

    for cluster_id in summary.index:
        print(f"Cluster {cluster_id}: {strategies.get(cluster_id)}")


# -------------------------------
# Step 6: Visualization
# -------------------------------

def plot_and_save(df, model, scaler):
    plt.figure(figsize=(8, 6))

    for cluster_id in sorted(df["cluster"].unique()):
        cluster_data = df[df["cluster"] == cluster_id]
        plt.scatter(
            cluster_data["annual_income_k"],
            cluster_data["spending_score"],
            label=f"Cluster {cluster_id}"
        )

    # Plot centroids
    centers = scaler.inverse_transform(model.cluster_centers_)
    plt.scatter(
        centers[:, 0],
        centers[:, 1],
        s=200,
        marker='X',
        label='Centroids'
    )

    plt.xlabel("Annual Income (k)")
    plt.ylabel("Spending Score")
    plt.title("Customer Segmentation using K-Means")
    plt.legend()
    plt.grid()

    # Save plot
    plt.savefig("customer_segments.png")

    print("\n[Scatter plot saved as 'customer_segments.png']")

    plt.show()


# -------------------------------
# Main Program
# -------------------------------

def main():
    print("=== Customer Segmentation using K-Means ===\n")

    # Create dataset
    df = generate_data()
    print("Dataset Sample:")
    print(df.head())

    # Scale data
    scaled_data, scaler = scale_features(df)

    # Apply clustering
    model, labels = perform_clustering(scaled_data, k=5)
    df["cluster"] = labels

    # Summary
    summary = cluster_summary(df)

    print("\n--- Cluster Summary ---")
    print(summary.to_string())

    # Business strategies
    print_strategies(summary)

    # Visualization
    plot_and_save(df, model, scaler)


# Run program
if __name__ == "__main__":
    main()