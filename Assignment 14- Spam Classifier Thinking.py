# Assignment 14: Spam Classifier Thinking
# Date: 10/03/2026

print("=" * 70)
print("        SPAM CLASSIFIER THINKING — SYSTEM DESIGN")
print("=" * 70)


# -------------------------------
# Step 1: Features (Model Inputs)
# -------------------------------
features = [
    "Word frequency of spam keywords (free, win, prize, urgent)",
    "Presence of URLs / number of links",
    "Use of ALL CAPS words",
    "Exclamation mark count (!)",
    "Sender email domain reputation",
    "Message length (very short or very long)",
    "Number of special characters ($, *, !)",
    "TF-IDF scores of important words/phrases",
    "Sender in contact list (yes/no)",
    "Time of message (odd hours vs normal)"
]

print("\n--- FEATURES (Inputs to Model) ---")
for i, f in enumerate(features, 1):
    print(f"{i:>2}. {f}")


# -------------------------------
# Step 2: Data Requirements
# -------------------------------
data_needed = [
    "Labeled dataset (Spam = 1, Ham = 0)",
    "At least ~10,000 messages for good performance",
    "Balanced dataset (handle imbalance if needed)",
    "Text preprocessing (tokenization, stopwords removal, stemming)",
    "Train / Validation / Test split (70 / 15 / 15)"
]

print("\n--- DATA REQUIREMENTS ---")
for d in data_needed:
    print(f" - {d}")


# -------------------------------
# Step 3: Possible Mistakes
# -------------------------------
mistakes = {
    "False Positive": "Legitimate message marked as spam (important mail lost)",
    "False Negative": "Spam message marked as normal (dangerous)",
    "Overfitting": "Model performs well on training but fails on new data",
    "Data Bias": "Model fails on new types of spam",
    "Class Imbalance": "Model predicts only majority class (misleading accuracy)"
}

print("\n--- POSSIBLE MISTAKES ---")
for k, v in mistakes.items():
    print(f"{k:<18}: {v}")


# -------------------------------
# Step 4: Recommended Approach
# -------------------------------
print("\n--- RECOMMENDED APPROACH ---")
print(" Algorithm : Naive Bayes (baseline) or Logistic Regression")
print(" Evaluation: Precision, Recall, F1-Score (focus on spam detection)")
print(" Threshold : Tune carefully to reduce false positives")


# -------------------------------
# Step 5: Conclusion
# -------------------------------
print("\n--- CONCLUSION ---")
print(" A good spam classifier balances accuracy and user safety.")
print(" Minimizing false positives is critical to avoid losing important emails.")