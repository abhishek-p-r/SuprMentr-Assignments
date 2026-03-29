# ==========================================
# Assignment 12: KNN in Real Life - Netflix Recommendations
# Date: 07/03/2026
# ==========================================

import math


# -------------------------------
# Step 1: Movie Dataset
# -------------------------------

def get_movies():
    return {
        "Inception":       {"Action":1,"Comedy":0,"Drama":1,"SciFi":1,"Romance":0},
        "The Notebook":    {"Action":0,"Comedy":0,"Drama":1,"SciFi":0,"Romance":1},
        "Avengers":        {"Action":1,"Comedy":1,"Drama":0,"SciFi":1,"Romance":0},
        "La La Land":      {"Action":0,"Comedy":1,"Drama":1,"SciFi":0,"Romance":1},
        "Interstellar":    {"Action":1,"Comedy":0,"Drama":1,"SciFi":1,"Romance":0},
        "Titanic":         {"Action":0,"Comedy":0,"Drama":1,"SciFi":0,"Romance":1},
        "Iron Man":        {"Action":1,"Comedy":1,"Drama":0,"SciFi":1,"Romance":0},
        "Pride&Prejudice": {"Action":0,"Comedy":0,"Drama":1,"SciFi":0,"Romance":1}
    }


# -------------------------------
# Step 2: User Preferences
# -------------------------------

def get_user_profile():
    return {
        "Action": 1,
        "Comedy": 0,
        "Drama": 1,
        "SciFi": 1,
        "Romance": 0
    }


# -------------------------------
# Step 3: Distance Function
# -------------------------------

def euclidean_distance(a: dict, b: dict) -> float:
    """Calculate Euclidean distance"""
    return math.sqrt(sum((a[key] - b[key]) ** 2 for key in a))


# -------------------------------
# Step 4: KNN Recommendation
# -------------------------------

def knn_recommend(user_profile: dict, movies: dict, k: int = 3):
    """Return top-k nearest movies"""

    distances = {}

    for title, features in movies.items():
        distance = euclidean_distance(user_profile, features)
        distances[title] = round(distance, 4)

    # Sort movies by distance (ascending)
    sorted_movies = sorted(distances.items(), key=lambda item: item[1])

    # Return top-k recommendations
    return sorted_movies[:k], distances


# -------------------------------
# Step 5: Display Output
# -------------------------------

def display_results(user_profile: dict, recommendations: list, distances: dict):
    print("=" * 70)
    print("      KNN NETFLIX-LIKE RECOMMENDATION SYSTEM")
    print("=" * 70)

    print("\nUser Preferences:")
    print(user_profile)

    print("\n--- All Movie Distances ---")

    recommended_titles = [title for title, _ in recommendations]

    for title, dist in sorted(distances.items(), key=lambda item: item[1]):
        marker = " <-- RECOMMENDED" if title in recommended_titles else ""
        print(f"{title:<22} : Distance = {dist:.4f}{marker}")

    print("\n--- Top Recommendations ---")

    for i, (title, dist) in enumerate(recommendations, start=1):
        print(f"{i}. {title} (Distance = {dist:.4f})")


# -------------------------------
# Main Function
# -------------------------------

def main():
    movies = get_movies()
    user_profile = get_user_profile()

    recommendations, distances = knn_recommend(user_profile, movies, k=3)

    display_results(user_profile, recommendations, distances)


# Entry Point
if __name__ == "__main__":
    main()