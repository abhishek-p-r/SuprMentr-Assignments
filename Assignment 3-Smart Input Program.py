# ==========================================
# Assignment 3: Smart Input Program
# Date: 12/02/2026
# ==========================================

# -------------------------------
# Logic Functions
# -------------------------------

def categorize_age(age: int) -> str:
    """Categorize age into groups"""
    if age < 0:
        return "Invalid"
    elif age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    elif age <= 25:
        return "Young Adult"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior Citizen"


def generate_message(name: str, age: int, hobby: str) -> tuple:
    """Generate personalized message based on age category"""
    category = categorize_age(age)

    messages = {
        "Child": f"Hey {name}! At {age}, every day is an adventure. Keep enjoying {hobby}!",
        "Teenager": f"Hey {name}! {age} is full of possibilities. {hobby} sounds exciting!",
        "Young Adult": f"Hi {name}! At {age}, you are shaping your future. Keep going with {hobby}!",
        "Adult": f"Hello {name}! Managing life at {age} while enjoying {hobby} is impressive!",
        "Senior Citizen": f"Dear {name}, your passion for {hobby} at {age} is truly inspiring!",
        "Invalid": f"Hi {name}, please enter a valid age."
    }

    return category, messages.get(category, "Hello!")


# -------------------------------
# Input Functions
# -------------------------------

def get_valid_name() -> str:
    """Get non-empty name input"""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def get_valid_age() -> int:
    """Get valid integer age"""
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Please enter a valid whole number.")


def get_valid_hobby() -> str:
    """Get non-empty hobby input"""
    while True:
        hobby = input("Enter your hobby: ").strip()
        if hobby:
            return hobby
        print("Hobby cannot be empty. Please try again.")


# -------------------------------
# Display Function
# -------------------------------

def display_result(name: str, age: int, category: str, hobby: str, message: str):
    """Display formatted output"""
    print("\n" + "=" * 55)
    print(f"{'Name':<12}: {name}")
    print(f"{'Age':<12}: {age}")
    print(f"{'Category':<12}: {category}")
    print(f"{'Hobby':<12}: {hobby}")
    print("=" * 55)

    print("\nPersonalized Message:")
    print(f"  {message}")


# -------------------------------
# Main Function
# -------------------------------

def main():
    print("=== Smart Input Program ===\n")

    name = get_valid_name()
    age = get_valid_age()
    hobby = get_valid_hobby()

    category, message = generate_message(name, age, hobby)

    display_result(name, age, category, hobby, message)


# Entry Point
if __name__ == "__main__":
    main()