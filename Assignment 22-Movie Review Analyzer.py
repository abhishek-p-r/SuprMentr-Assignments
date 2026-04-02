"""
Assignment 22: Movie Review Analyzer - Simple Sentiment Analyzer
Date: 26/03/2026
"""

import re

# -------------------------------
# 🎬 Movie Reviews
# -------------------------------
REVIEWS = [
    ("The Dark Knight",
     "An absolutely masterful film. Heath Ledger's Joker is terrifyingly brilliant and the story "
     "is gripping from start to finish. Christopher Nolan delivers a perfect, unforgettable masterpiece."),

    ("Cats (2019)",
     "Horrible and deeply unsettling. The CGI is nightmarish, the plot makes no sense, and "
     "the characters are bizarre. A terrible disappointment that is painful to watch."),

    ("Inception",
     "A mind-bending, visually stunning thriller. The concept is brilliant and the execution is "
     "impressive. Some scenes are confusing but overall an outstanding cinematic experience."),

    ("Transformers: Age of Extinction",
     "Loud, boring and unnecessarily long. The plot is weak, acting is mediocre, and "
     "there is no real story. Just explosions and noise. Completely forgettable film."),

    ("Interstellar",
     "A visually gorgeous and emotionally powerful sci-fi epic. The science is fascinating, "
     "though some parts are slow and the ending is slightly confusing. Still a remarkable film."),
]

# -------------------------------
# 😊 Positive Words
# -------------------------------
POS_WORDS = {
    "masterful","brilliant","perfect","outstanding","stunning","gorgeous","powerful",
    "excellent","amazing","wonderful","great","good","fantastic","impressive","remarkable",
    "gripping","unforgettable","fascinating","best","love","loved","terrific","superb",
}

# -------------------------------
# 😡 Negative Words
# -------------------------------
NEG_WORDS = {
    "horrible","terrible","awful","bad","boring","weak","mediocre","disappointing",
    "nightmarish","unsettling","painful","forgettable","poor","worst","confusing",
    "slow","loud","bizarre","dull","waste","wasted",
}

# -------------------------------
# 🚫 Negation Words
# -------------------------------
NEGATORS = {"not", "no", "never", "didn't", "doesn't", "isn't"}

# -------------------------------
# 🔍 Sentiment Analysis Function
# -------------------------------
def analyze_review(text):
    tokens = re.findall(r"[a-z']+", text.lower())

    pos_count = 0
    neg_count = 0

    for i, word in enumerate(tokens):
        prev_word = tokens[i - 1] if i > 0 else ""
        is_negated = prev_word in NEGATORS

        # Positive word
        if word in POS_WORDS:
            if is_negated:
                neg_count += 1
            else:
                pos_count += 1

        # Negative word
        elif word in NEG_WORDS:
            if is_negated:
                pos_count += 1
            else:
                neg_count += 1

    # Sentiment Score
    total = pos_count + neg_count
    score = (pos_count - neg_count) / max(total, 1)

    # Label Decision
    if score > 0.2:
        label = "POSITIVE"
    elif score < -0.1:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"

    return pos_count, neg_count, round(score, 3), label

# -------------------------------
# 🚀 Main Execution
# -------------------------------
print("\n" + "=" * 70)
print("  ASSIGNMENT 22: MOVIE REVIEW ANALYZER")
print("=" * 70)

for movie, review in REVIEWS:
    pos, neg, score, label = analyze_review(review)

    # Visual Meter
    positive_bar = "+" * pos
    negative_bar = "-" * neg

    print(f"\n🎬 Movie   : {movie}")
    print(f"📝 Review  : {review[:70]}...")
    print(f"👍 Pos hits: {pos}  |  👎 Neg hits: {neg}")
    print(f"📊 Score   : {score:+.3f}  |  [{label}]")
    print(f"📈 Meter   : [{positive_bar}{negative_bar}]")