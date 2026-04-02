"""
Assignment 21: Word Importance Explorer - TF-IDF on 5 Documents
Date: 24/03/2026
"""

import math
import re
from collections import Counter

# -------------------------------
# 📄 Documents
# -------------------------------
DOCUMENTS = {
    "Doc1_AI": (
        "Artificial intelligence and machine learning are transforming technology. "
        "Deep learning neural networks enable computers to recognize images and speech. "
        "Machine learning algorithms learn from data automatically."
    ),

    "Doc2_Climate": (
        "Climate change causes rising sea levels and extreme weather events. "
        "Global warming increases temperatures worldwide due to greenhouse gases. "
        "Carbon emissions from fossil fuels accelerate climate change."
    ),

    "Doc3_Health": (
        "Regular exercise improves cardiovascular health and mental wellbeing. "
        "A balanced diet with vitamins and minerals prevents diseases. "
        "Sleep is essential for physical health and cognitive function."
    ),

    "Doc4_Space": (
        "NASA's space missions explore planets and galaxies in the universe. "
        "Astronomers study black holes, stars, and cosmic radiation. "
        "Space telescopes capture stunning images of distant nebulae and galaxies."
    ),

    "Doc5_Finance": (
        "Stock markets fluctuate based on economic indicators and investor sentiment. "
        "Inflation affects purchasing power and interest rates in the economy. "
        "Diversified investment portfolios reduce financial risk over time."
    ),
}

# -------------------------------
# 🚫 Stopwords
# -------------------------------
STOPWORDS = {
    "a","an","the","and","or","but","in","on","at","to","for","of","with",
    "is","are","was","were","be","been","from","by","as","that","this",
    "it","its","their","they","due","over","into","also"
}

# -------------------------------
# 🧹 Tokenization
# -------------------------------
def tokenize(text):
    words = re.findall(r"[a-z]+", text.lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

# -------------------------------
# 📊 Term Frequency (TF)
# -------------------------------
def compute_tf(tokens):
    word_count = Counter(tokens)
    total_words = len(tokens)

    tf = {}
    for word, count in word_count.items():
        tf[word] = count / total_words

    return tf

# -------------------------------
# 🌍 Inverse Document Frequency (IDF)
# -------------------------------
def compute_idf(all_tokens):
    N = len(all_tokens)
    idf = {}

    # Unique words across all documents
    unique_words = set(word for tokens in all_tokens for word in tokens)

    for word in unique_words:
        doc_freq = sum(1 for tokens in all_tokens if word in tokens)
        idf[word] = math.log(N / doc_freq) + 1

    return idf

# -------------------------------
# 🚀 Main Execution
# -------------------------------

# Tokenize all documents
docs_tokens = {
    name: tokenize(text)
    for name, text in DOCUMENTS.items()
}

# Compute IDF
idf = compute_idf(list(docs_tokens.values()))

# Compute TF-IDF and extract Top 5 words
results = {}

for doc_name, tokens in docs_tokens.items():
    tf = compute_tf(tokens)

    tfidf_scores = {
        word: round(tf[word] * idf[word], 4)
        for word in tf
    }

    # Sort by highest score, then alphabetically
    top_words = sorted(
        tfidf_scores.items(),
        key=lambda x: (-x[1], x[0])
    )[:5]

    results[doc_name] = top_words

# -------------------------------
# 🖨️ Output
# -------------------------------
print("\n" + "=" * 60)
print("  ASSIGNMENT 21: WORD IMPORTANCE EXPLORER (TF-IDF)")
print("=" * 60)

print(f"\n{'Document':<18} {'Rank':<6} {'Keyword':<20} {'TF-IDF Score'}")
print("-" * 56)

for doc, words in results.items():
    for rank, (word, score) in enumerate(words, start=1):
        doc_display = doc if rank == 1 else ""
        print(f"{doc_display:<18} {rank:<6} {word:<20} {score:.4f}")
    print()