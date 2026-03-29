# ==========================================
# Assignment 19: Text Challenges
# Date: 20/03/2026
# ==========================================

import re
import string


# -------------------------------
# Step 1: Dataset (Messy Sentences)
# -------------------------------

def get_sentences():
    return [
        "omg dis movie was soooo lit frfr",
        "i luv u 2 babe cant wait 4 tmrw",
        "wut r u doin?? lmaooo",
        "teh cat sat on teh matt",
        "I recieve alot of mails its wierd",
        "tbh ur outfit is lowkey goals ngl",
        "yoooo the vibes r immaculate bestie",
        "cant believe he ghosted her smh",
        "gonna b late but its fine ig",
        "the wether was gr8 4 a picnik!!",
        "STOP YELLING AT ME IM FINE",
        "their going to there house over they're",
        "no way thiss is happenning rn omgggg",
        "u rlly think ur better than me??",
        "lol k whatever dude idc",
        "3 coffees in n i still cant focuusss",
        "bro this hits different fr no cap",
        "shes so extra all the time periodt",
        "jst got bck frm th gym nd im ded",
        "she said she gonna b here at 2 ig lol",
    ]


# -------------------------------
# Step 2: Define Patterns
# -------------------------------

SLANG_WORDS = {
    'omg','dis','frfr','luv','u','2','4','tmrw','wut','r','lmaooo',
    'tbh','ngl','yoooo','smh','ig','gr8','rn','rlly','lol','idc',
    'bro','periodt','ded','jst','bck','frm','nd','gonna','lowkey',
    'vibes','bestie','ghosted','ur'
}

TYPO_WORDS = {
    'teh','recieve','alot','wierd','happenning','thiss',
    'focuusss','wether','picnik','matt'
}


# -------------------------------
# Step 3: Text Cleaning Helper
# -------------------------------

def tokenize(text: str):
    text = text.lower()
    text = re.sub(rf"[{re.escape(string.punctuation)}]", "", text)
    return text.split()


# -------------------------------
# Step 4: Classification Logic
# -------------------------------

def classify_text(sentence: str) -> str:
    issues = []

    tokens = tokenize(sentence)

    # Check slang
    if any(word in SLANG_WORDS for word in tokens):
        issues.append("SLANG")

    # Check typos
    if any(word in TYPO_WORDS for word in tokens):
        issues.append("TYPO")

    # Check ALL CAPS
    if sentence.isupper():
        issues.append("ALL-CAPS")

    # Check emoji / non-ascii
    if any(ord(char) > 127 for char in sentence):
        issues.append("EMOJI")

    # Default case
    if not issues:
        issues.append("INFORMAL")

    return " + ".join(issues)


# -------------------------------
# Step 5: Display Results
# -------------------------------

def display_results(sentences):
    print("=" * 80)
    print("              TEXT CHALLENGES - ISSUE CLASSIFICATION")
    print("=" * 80)

    print(f"{'No.':<5} {'Sentence':<50} {'Issue Type'}")
    print("-" * 80)

    for i, sentence in enumerate(sentences, start=1):
        issue_type = classify_text(sentence)
        print(f"{i:<5} {sentence[:48]:<50} {issue_type}")


# -------------------------------
# Main Function
# -------------------------------

def main():
    sentences = get_sentences()
    display_results(sentences)


# Entry Point
if __name__ == "__main__":
    main()