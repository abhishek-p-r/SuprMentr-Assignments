# Assignment 9: Storytelling with Graphs
# Date: 28/02/2026

import matplotlib.pyplot as plt
import numpy as np


# -------------------------------
# Step 1: Dataset
# -------------------------------
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales  = [4200, 3800, 5100, 6200, 5700, 7100]

products   = ['Electronics', 'Clothing', 'Food', 'Books', 'Toys']
market_pct = [35, 25, 20, 12, 8]

student_scores = [45,52,58,61,65,67,70,72,74,76,
                  78,80,82,83,85,87,90,91,93,95]


# -------------------------------
# Step 2: Create Subplots
# -------------------------------
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle("Sales & Academic Data Story",
             fontsize=14, fontweight='bold')


# -------------------------------
# Chart 1: Bar Chart (Sales)
# -------------------------------
colors = ['#2196F3' if s < max(sales) else '#4CAF50' for s in sales]

axes[0].bar(months, sales, color=colors, edgecolor='white')
axes[0].set_title("Monthly Sales (Jan–Jun)", fontweight='bold')
axes[0].set_ylabel("Sales (Units)")

# Add values on bars
for i, v in enumerate(sales):
    axes[0].text(i, v + 80, str(v), ha='center', fontsize=9)


# -------------------------------
# Chart 2: Pie Chart (Market Share)
# -------------------------------
axes[1].pie(
    market_pct,
    labels=products,
    autopct='%1.1f%%',
    startangle=140
)
axes[1].set_title("Product Market Share", fontweight='bold')


# -------------------------------
# Chart 3: Histogram (Scores)
# -------------------------------
mean_score = np.mean(student_scores)

axes[2].hist(
    student_scores,
    bins=8,
    color='#7C4DFF',
    edgecolor='white',
    alpha=0.85
)

axes[2].set_title("Student Score Distribution", fontweight='bold')

# Mean line
axes[2].axvline(
    mean_score,
    color='red',
    linestyle='--',
    label=f'Mean = {mean_score:.1f}'
)
axes[2].legend()


# -------------------------------
# Step 3: Layout & Save
# -------------------------------
plt.tight_layout()
plt.savefig("storytelling_graphs.png", dpi=150, bbox_inches='tight')
plt.show()


# -------------------------------
# Step 4: Data Story Insights
# -------------------------------
print("=" * 60)
print("                DATA STORY INSIGHTS")
print("=" * 60)

growth = ((sales[-1] - sales[0]) / sales[0]) * 100

print(f"1. SALES  : Increased by {growth:.1f}% from Jan to Jun.")
print("            Dip in Feb, followed by steady growth.")

print("2. MARKET : Electronics dominates with 35%.")
print("            Top 2 categories contribute ~60% of total share.")

print(f"3. SCORES : Nearly normal distribution.")
print(f"            Average score ≈ {mean_score:.1f}")