# ==========================================
# Assignment 4: Logic Builder - FizzBuzz
# Date: 17/02/2026
# ==========================================

# -------------------------------
# Core Logic
# -------------------------------

def generate_fizzbuzz(limit: int) -> tuple:
    """Generate FizzBuzz results and count occurrences"""
    
    results = []
    counts = {
        "Fizz": 0,
        "Buzz": 0,
        "FizzBuzz": 0,
        "Number": 0
    }

    for num in range(1, limit + 1):

        if num % 15 == 0:
            label = "FizzBuzz"
            counts["FizzBuzz"] += 1

        elif num % 3 == 0:
            label = "Fizz"
            counts["Fizz"] += 1

        elif num % 5 == 0:
            label = "Buzz"
            counts["Buzz"] += 1

        else:
            label = str(num)
            counts["Number"] += 1

        results.append((num, label))

    return results, counts


# -------------------------------
# Display Output
# -------------------------------

def display_results(results: list, counts: dict):
    """Display formatted FizzBuzz output"""

    print("=== FizzBuzz Output (1 to 50) ===\n")

    row = []

    for num, label in results:
        row.append(f"{label:>8}")

        # Print 5 items per row
        if num % 5 == 0:
            print("  " + "  ".join(row))
            row.clear()

    print("\n--- Occurrence Summary ---")

    for key, value in counts.items():
        print(f"{key:<12}: {value}")

    print(f"{'Total':<12}: {sum(counts.values())}")


# -------------------------------
# Main Function
# -------------------------------

def main():
    LIMIT = 50
    results, counts = generate_fizzbuzz(LIMIT)
    display_results(results, counts)


# Entry Point
if __name__ == "__main__":
    main()