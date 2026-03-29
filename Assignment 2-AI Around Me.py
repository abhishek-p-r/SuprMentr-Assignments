# ==========================================
# Assignment 2: AI Around Me
# Date: 09/02/2026
# ==========================================

# List of AI Applications
ai_applications = [
    {
        "id": 1,
        "name": "Google Search",
        "description": "Uses BERT (NLP Transformer) to understand search intent and rank results."
    },
    {
        "id": 2,
        "name": "YouTube Recommendations",
        "description": "Uses collaborative filtering and deep learning to suggest videos."
    },
    {
        "id": 3,
        "name": "Gmail Spam Filter",
        "description": "Uses Naive Bayes classifier to detect spam emails."
    },
    {
        "id": 4,
        "name": "Face Unlock (Smartphone)",
        "description": "Uses CNN to recognize facial features for authentication."
    },
    {
        "id": 5,
        "name": "Google Maps / Navigation",
        "description": "Uses ML models to predict traffic and suggest optimal routes."
    },
    {
        "id": 6,
        "name": "Netflix / Hotstar",
        "description": "Uses recommendation systems to match user preferences with content."
    },
    {
        "id": 7,
        "name": "Google Assistant / Siri",
        "description": "Uses speech recognition and NLP to understand and respond."
    },
    {
        "id": 8,
        "name": "Instagram Reels Feed",
        "description": "Uses reinforcement learning to rank engaging content."
    },
    {
        "id": 9,
        "name": "Bank Fraud Detection",
        "description": "Uses anomaly detection to identify unusual transactions."
    },
    {
        "id": 10,
        "name": "Autocorrect / Predictive Text",
        "description": "Uses language models to predict and correct words."
    }
]


# -------------------------------
# Display Function
# -------------------------------

def display_ai_apps(apps: list):
    """Display AI applications in a formatted way"""

    print("=" * 70)
    print(f"{'AI Applications Around Me':^70}")
    print("=" * 70)

    for app in apps:
        print(f"\n{app['id']:2}. {app['name']}")
        print(f"   → ML Concept: {app['description']}")

    print("\n" + "=" * 70)
    print(f"Total Applications: {len(apps)}")
    print("=" * 70)


# -------------------------------
# Main Function
# -------------------------------

def main():
    display_ai_apps(ai_applications)


# Entry Point
if __name__ == "__main__":
    main()