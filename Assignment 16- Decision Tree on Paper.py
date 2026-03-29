# ==========================================
# Assignment 16: Decision Tree on Paper
# Date: 12/03/2026
# ==========================================


# -------------------------------
# Decision Function
# -------------------------------

def should_play_outside(weather: str, temperature: str, wind: str, humidity: str):
    """
    Decision Tree Logic:
    Weather?
      Rainy  -> NO
      Cloudy -> Wind Strong? -> NO | Weak? -> YES
      Sunny  -> Temp?
                 Mild -> YES
                 Hot  -> Humidity High? -> NO | Low? -> YES
                 Cold -> Wind Strong? -> NO | Weak? -> YES
    """

    # Weather condition
    if weather == "Rainy":
        return "NO", "Rainy weather - better stay inside"

    elif weather == "Cloudy":
        if wind == "Strong":
            return "NO", "Cloudy with strong wind"
        else:
            return "YES", "Cloudy but calm - safe to go"

    elif weather == "Sunny":

        # Temperature condition
        if temperature == "Mild":
            return "YES", "Pleasant sunny weather"

        elif temperature == "Hot":
            if humidity == "High":
                return "NO", "Too hot and humid"
            else:
                return "YES", "Hot but dry weather"

        elif temperature == "Cold":
            if wind == "Strong":
                return "NO", "Cold and windy"
            else:
                return "YES", "Cold but calm"

    # Default case
    return "YES", "Conditions acceptable"


# -------------------------------
# Test Cases
# -------------------------------

def run_test_cases():
    test_cases = [
        ("Sunny",  "Mild",  "Weak",   "Low"),
        ("Sunny",  "Hot",   "Weak",   "High"),
        ("Sunny",  "Hot",   "Weak",   "Low"),
        ("Sunny",  "Cold",  "Strong", "Low"),
        ("Sunny",  "Cold",  "Weak",   "Low"),
        ("Cloudy", "Mild",  "Weak",   "Normal"),
        ("Cloudy", "Mild",  "Strong", "Normal"),
        ("Rainy",  "Mild",  "Weak",   "High"),
    ]

    print("=== Decision Tree: Should I Play Outside? ===\n")

    print(f"{'#':<4}{'Weather':<10}{'Temp':<8}{'Wind':<10}{'Humidity':<10}{'Result'}")
    print("-" * 70)

    for i, (w, t, wi, h) in enumerate(test_cases, start=1):
        result, reason = should_play_outside(w, t, wi, h)
        print(f"{i:<4}{w:<10}{t:<8}{wi:<10}{h:<10}{result}  [{reason}]")


# -------------------------------
# Display Tree Structure
# -------------------------------

def print_tree():
    print("\n--- Decision Tree Structure ---\n")

    print("Weather?")
    print("|-- Rainy              => NO")
    print("|-- Cloudy")
    print("|     |-- Wind=Strong  => NO")
    print("|     +-- Wind=Weak    => YES")
    print("+-- Sunny")
    print("      |-- Temp=Mild    => YES")
    print("      |-- Temp=Hot")
    print("      |     |-- Humidity=High => NO")
    print("      |     +-- Humidity=Low  => YES")
    print("      +-- Temp=Cold")
    print("            |-- Wind=Strong   => NO")
    print("            +-- Wind=Weak     => YES")


# -------------------------------
# Main Function
# -------------------------------

def main():
    run_test_cases()
    print_tree()


# Entry Point
if __name__ == "__main__":
    main()