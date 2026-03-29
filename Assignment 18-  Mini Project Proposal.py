# Assignment 19: Mini Project Proposal (Sentiment Analysis)
# Date: 19/03/2026

import pandas as pd
import numpy as np
import re
import string

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# -------------------------------
# Step 1: Text Preprocessing
# -------------------------------
def clean_review(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', '', text)   # remove URLs
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()     # remove extra spaces
    return text


# -------------------------------
# Step 2: Create Dataset (Fixed)
# -------------------------------
np.random.seed(42)

positive = [
    "great product love it",
    "excellent quality highly recommend",
    "works perfectly amazing value",
    "best purchase ever fantastic"
]

negative = [
    "terrible waste of money",
    "broke after one day very disappointed",
    "poor quality do not buy",
    "horrible experience never again"
]

neutral = [
    "it is okay average quality",
    "decent product nothing special",
    "met expectations nothing more",
    "average works as described"
]

# Create balanced dataset safely
texts = []
labels = []

for _ in range(500):
    for p in positive:
        texts.append(p)
        labels.append('positive')

    for n in negative:
        texts.append(n)
        labels.append('negative')

    for u in neutral:
        texts.append(u)
        labels.append('neutral')

# Convert to DataFrame
df = pd.DataFrame({
    'review': texts,
    'sentiment': labels
})

# Shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Clean text
df['clean'] = df['review'].apply(clean_review)


# -------------------------------
# Step 3: TF-IDF Vectorization
# -------------------------------
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['clean'])
y = df['sentiment']


# -------------------------------
# Step 4: Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -------------------------------
# Step 5: Train Model
# -------------------------------
model = MultinomialNB(alpha=0.1)
model.fit(X_train, y_train)


# -------------------------------
# Step 6: Evaluation
# -------------------------------
y_pred = model.predict(X_test)

print("=== Model Evaluation ===")
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# -------------------------------
# Step 7: Prediction Function
# -------------------------------
def predict_sentiment(review):
    cleaned = clean_review(review)
    vector  = vectorizer.transform([cleaned])
    return model.predict(vector)[0]


# -------------------------------
# Step 8: Demo Predictions
# -------------------------------
print("\n=== Demo Predictions ===")

samples = [
    "This product is absolutely fantastic!",
    "Worst purchase I have ever made.",
    "It is okay, nothing special."
]

for s in samples:
    result = predict_sentiment(s)
    print(f"  '{s[:45]}...' → {result.upper()}")