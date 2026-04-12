"""
Assignment 26: NLP Mini App - Keyword Extractor Chatbot (Final Version)
Date: 03/04/2026
"""

import re
import math
from collections import Counter

# -----------------------------
# 🧹 Stopwords
# -----------------------------
STOPWORDS = {
    "a","an","the","and","or","but","in","on","at","to","for","of","with",
    "is","are","was","were","be","been","from","by","as","that","this","it",
    "its","they","their","we","you","do","did","does","has","have","had",
    "will","would","can","could","not","no","so","if","also","just","very",
}

# -----------------------------
# 📚 Reference Corpus
# -----------------------------
CORPUS = [
    "technology science research development innovation engineering",
    "health medicine disease treatment patient doctor hospital",
    "economy finance market investment business trade company",
    "education school university student teacher learning knowledge",
    "environment climate nature planet earth energy pollution",
    "politics government law policy election democracy society",
]

# -----------------------------
# 🔍 Text Preprocessing
# -----------------------------
def tokenize(text):
    words = re.findall(r"[a-z]+", text.lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

# -----------------------------
# 🧠 TF-IDF Calculation
# -----------------------------
def compute_tfidf(user_text, top_n=8):
    tokens = tokenize(user_text)

    # ✅ FIX: Always return 4 values
    if not tokens:
        return [], {}, Counter(), 0

    documents = CORPUS + [" ".join(tokens)]
    tokenized_docs = [tokenize(doc) for doc in documents]
    N = len(tokenized_docs)

    vocab = set(tokens)

    # IDF
    idf = {}
    for word in vocab:
        doc_count = sum(1 for doc in tokenized_docs if word in doc)
        idf[word] = round(math.log(N / max(doc_count, 1)) + 1, 4)

    # TF
    word_counts = Counter(tokens)
    total_words = len(tokens)

    # TF-IDF
    tfidf = {}
    for word, count in word_counts.items():
        tf = count / total_words
        tfidf[word] = round(tf * idf[word], 4)

    top_keywords = sorted(tfidf.items(), key=lambda x: -x[1])[:top_n]

    return top_keywords, idf, word_counts, total_words

# -----------------------------
# 📊 Display Results
# -----------------------------
def display_results(label, text):
    print("\n" + "="*70)
    print(f"INPUT [{label}]: {text[:80]}...")

    top_kws, idf_map, count_map, total = compute_tfidf(text)

    # ✅ Better handling for short/invalid input
    if total == 0:
        print("⚠️ No meaningful keywords found. Try a longer sentence.")
        return

    print(f"\nTOP {len(top_kws)} KEYWORDS:\n")
    print(f"{'Rank':<6}{'Keyword':<20}{'TF-IDF':<10}{'Freq':<8}{'Bar'}")
    print("-"*60)

    for rank, (word, score) in enumerate(top_kws, 1):
        bar = "█" * min(int(score * 40), 20)
        print(f"{rank:<6}{word:<20}{score:<10.4f}{count_map[word]:<8}{bar}")

    print("\nTF × IDF Breakdown (Top 3):")
    for word, score in top_kws[:3]:
        tf = round(count_map[word] / total, 4)
        print(f"'{word}': TF={tf} × IDF={idf_map[word]} = {score}")

# -----------------------------
# 🧪 Sample Inputs
# -----------------------------
SAMPLE_INPUTS = [
    ("AI_Healthcare",
     "Artificial intelligence and deep learning are transforming modern healthcare. "
     "Machine learning models detect cancer from medical images with high accuracy."),

    ("Climate_Change",
     "Climate change is accelerating melting ice caps and rising sea levels. "
     "Renewable energy like solar and wind can reduce carbon emissions."),

    ("Crypto_Blockchain",
     "Cryptocurrency and blockchain are disrupting finance. "
     "Bitcoin enables decentralized transactions without banks."),
]

# -----------------------------
# 🚀 Main Program
# -----------------------------
def main():
    print("\n" + "="*70)
    print("   NLP MINI APP: KEYWORD EXTRACTOR CHATBOT")
    print("="*70)

    # Run sample inputs
    for label, text in SAMPLE_INPUTS:
        display_results(label, text)

    print("\nEnter your own text (type 'exit' to quit):\n")

    # Interactive chatbot loop
    while True:
        user_input = input(">> ").strip()

        if user_input.lower() == "exit":
            print("Session ended.")
            break

        # Optional: handle very short inputs nicely
        if len(user_input) < 3:
            print("⚠️ Please enter a longer sentence.")
            continue

        display_results("USER_INPUT", user_input)

# -----------------------------
# ▶️ Run App
# -----------------------------
if __name__ == "__main__":
    main()