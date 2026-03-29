# ==========================================
# Assignment 20: Build a Text Cleaner
# Date: 21/03/2026
# ==========================================

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# -------------------------------
# Step 1: Setup (Download NLTK Data)
# -------------------------------

def setup_nltk():
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt', quiet=True)


# -------------------------------
# Step 2: Load Stopwords
# -------------------------------

def load_stopwords():
    return set(stopwords.words('english'))


# -------------------------------
# Step 3: Text Cleaning Pipeline
# -------------------------------

def clean_text(text: str, stop_words: set) -> str:
    """
    NLP Text Preprocessing Steps:
      1. Lowercase
      2. Remove URLs
      3. Remove punctuation
      4. Remove extra spaces
      5. Tokenize
      6. Remove stopwords
      7. Rejoin tokens
    """

    # 1. Lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # 3. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 4. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # 5. Tokenize
    tokens = word_tokenize(text)

    # 6. Remove stopwords
    cleaned_tokens = [word for word in tokens if word not in stop_words]

    # 7. Rejoin tokens
    return ' '.join(cleaned_tokens)


# -------------------------------
# Step 4: Test Sentences
# -------------------------------

def get_test_sentences():
    return [
        "Hello! This is a SAMPLE sentence with Punctuation, and STOP words.",
        "The quick brown fox jumps over the lazy dog.",
        "I absolutely LOVE this product! It is amazing and worth every penny.",
        "Visit our website at https://www.example.com for more info!",
        "She said, 'Don't worry about it,' and walked away calmly.",
        "Running, jumped, and quickly flies over beautiful mountains!!",
        "   Extra   spaces   and\ttabs   should be   removed   ",
        "The students ARE learning machine learning ALGORITHMS today.",
    ]


# -------------------------------
# Step 5: Display Results
# -------------------------------

def display_results(sentences, stop_words):
    print("=" * 70)
    print("        TEXT CLEANER — OUTPUT DEMONSTRATION")
    print("=" * 70)

    for i, sentence in enumerate(sentences, start=1):
        cleaned = clean_text(sentence, stop_words)

        print(f"\n[{i}] Original : {sentence.strip()}")
        print(f"    Cleaned  : {cleaned}")

    print("\n" + "=" * 70)
    print("All sentences processed successfully!")


# -------------------------------
# Main Function
# -------------------------------

def main():
    setup_nltk()
    stop_words = load_stopwords()
    sentences = get_test_sentences()
    display_results(sentences, stop_words)


# Entry Point
if __name__ == "__main__":
    main()