"""
Assignment 23: Semantic Meaning - Word Pair Cosine Similarity
Date: 27/03/2026
"""

import math

# ---------------------------------------
# 📊 Word Vectors (12 Semantic Features)
# ---------------------------------------
# [living, movement, cognitive, emotion, size, speed, nature,
#  tech, positive, negative, abstract, concrete]

WORD_VECTORS = {
    "king":     [0.1,0.2,0.6,0.3,0.8,0.1,0.0,0.0,0.8,0.1,0.6,0.9],
    "queen":    [0.1,0.2,0.6,0.4,0.7,0.1,0.0,0.0,0.8,0.1,0.6,0.9],

    "car":      [0.0,0.9,0.0,0.0,0.6,0.9,0.0,0.9,0.3,0.1,0.1,1.0],
    "bicycle":  [0.0,0.9,0.0,0.0,0.3,0.5,0.1,0.5,0.4,0.1,0.1,1.0],

    "happy":    [0.4,0.3,0.5,0.9,0.0,0.0,0.2,0.0,1.0,0.0,0.9,0.2],
    "sad":      [0.4,0.1,0.4,0.9,0.0,0.0,0.2,0.0,0.0,1.0,0.9,0.2],

    "dog":      [1.0,0.9,0.3,0.7,0.5,0.6,0.9,0.0,0.7,0.1,0.1,1.0],
    "wolf":     [1.0,0.9,0.3,0.4,0.7,0.8,1.0,0.0,0.3,0.6,0.1,1.0],

    "computer": [0.0,0.0,0.8,0.0,0.4,0.0,0.0,1.0,0.4,0.1,0.5,1.0],
    "brain":    [0.8,0.1,1.0,0.5,0.2,0.0,0.2,0.3,0.5,0.2,0.5,1.0],
}

# ---------------------------------------
# 🔗 Word Pairs with Meaning
# ---------------------------------------
PAIRS = [
    ("king",     "queen",    "Royalty - same hierarchy, differ by gender"),
    ("car",      "bicycle",  "Transport - both vehicles, differ in engine/size"),
    ("happy",    "sad",      "Emotion - opposite sentiments"),
    ("dog",      "wolf",     "Biology - same family, wild vs domestic"),
    ("computer", "brain",    "Cognition - artificial vs biological processing"),
]

# ---------------------------------------
# 📐 Cosine Similarity Function
# ---------------------------------------
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    magnitude_1 = math.sqrt(sum(a * a for a in vec1))
    magnitude_2 = math.sqrt(sum(b * b for b in vec2))

    return dot_product / (magnitude_1 * magnitude_2 + 1e-9)

# ---------------------------------------
# 🚀 Main Execution
# ---------------------------------------
print("\n" + "=" * 70)
print("  ASSIGNMENT 23: SEMANTIC MEANING -- WORD PAIR SIMILARITY")
print("=" * 70)

print(f"\n{'#':<4}{'Word 1':<12}{'Word 2':<12}{'Similarity':<14}{'Interpretation'}")
print("-" * 70)

for i, (word1, word2, meaning) in enumerate(PAIRS, start=1):

    similarity = cosine_similarity(
        WORD_VECTORS[word1],
        WORD_VECTORS[word2]
    )

    # Visual similarity bar
    bar_length = int(similarity * 20)
    bar = "#" * bar_length + "." * (20 - bar_length)

    print(f"{i:<4}{word1:<12}{word2:<12}{similarity:<14.4f}{meaning}")
    print(f"    Similarity bar: [{bar}] {similarity * 100:.1f}%\n")