# ==========================================
# Assignment 5: Student Data Manager
# Date: 19/02/2026
# ==========================================

# -------------------------------
# Student Data
# -------------------------------

students = {
    "Alice":   {"Math": 88, "Science": 92, "English": 76, "History": 85},
    "Bob":     {"Math": 70, "Science": 65, "English": 80, "History": 72},
    "Charlie": {"Math": 95, "Science": 98, "English": 91, "History": 94},
    "Diana":   {"Math": 60, "Science": 55, "English": 70, "History": 65},
    "Ethan":   {"Math": 78, "Science": 82, "English": 74, "History": 79}
}


# -------------------------------
# Utility Functions
# -------------------------------

def calculate_average(scores: dict) -> float:
    """Return average marks of a student"""
    return sum(scores.values()) / len(scores)


def assign_grade(avg: float) -> str:
    """Assign grade based on average"""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def calculate_class_average(data: dict) -> float:
    """Return overall class average"""
    total = sum(calculate_average(scores) for scores in data.values())
    return total / len(data)


def find_class_topper(data: dict) -> str:
    """Return name of class topper"""
    return max(data, key=lambda name: calculate_average(data[name]))


# -------------------------------
# Display Functions
# -------------------------------

def display_student_report(data: dict):
    """Display student report"""

    print("=" * 60)
    print(f"{'Student':<15}{'Average':>10}{'Grade':>10}")
    print("=" * 60)

    for name, scores in data.items():
        avg = calculate_average(scores)
        grade = assign_grade(avg)
        print(f"{name:<15}{avg:>10.2f}{grade:>10}")

    print("=" * 60)

    topper = find_class_topper(data)
    print(f"Class Topper  : {topper} ({calculate_average(data[topper]):.2f})")
    print(f"Class Average : {calculate_class_average(data):.2f}")

    print("=" * 60)


def display_subject_toppers(data: dict):
    """Display subject-wise toppers"""

    subjects = list(next(iter(data.values())).keys())

    print("\n--- Subject Toppers ---")

    for subject in subjects:
        topper = max(data, key=lambda name: data[name][subject])
        marks = data[topper][subject]
        print(f"{subject:<12}: {topper} ({marks})")


# -------------------------------
# Main Function
# -------------------------------

def main():
    print("=== Student Data Manager ===\n")

    display_student_report(students)
    display_subject_toppers(students)


# Entry Point
if __name__ == "__main__":
    main()