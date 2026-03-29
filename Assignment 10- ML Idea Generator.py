# Assignment 10: ML Idea Generator
# Date: 02/03/2026

# -------------------------------
# Step 1: ML Ideas Dictionary
# -------------------------------
ml_ideas = {
    "College": [
        {
            "problem": "Predict Student Dropout Risk",
            "input": "Attendance %, grades, assignment submission rate",
            "output": "Risk level: Low / Medium / High"
        },
        {
            "problem": "Smart Timetable Scheduler",
            "input": "Faculty availability, room capacity, student preferences",
            "output": "Optimized conflict-free timetable"
        },
        {
            "problem": "Plagiarism Detection",
            "input": "Student submission text, internet corpus",
            "output": "Similarity score + flagged sections"
        }
    ],

    "Healthcare": [
        {
            "problem": "Disease Diagnosis from Symptoms",
            "input": "Symptoms, age, medical history, test results",
            "output": "Probable diagnosis with confidence score"
        },
        {
            "problem": "Hospital Readmission Prediction",
            "input": "Discharge summary, vitals, medication history",
            "output": "Readmission probability (30 days)"
        },
        {
            "problem": "Medical Image Analysis (X-Ray/MRI)",
            "input": "Patient scan images",
            "output": "Detected anomaly + severity"
        }
    ],

    "Shopping": [
        {
            "problem": "Product Recommendation System",
            "input": "Browsing history, purchase history, ratings",
            "output": "Top-N personalized products"
        },
        {
            "problem": "Dynamic Pricing Optimization",
            "input": "Demand trends, competitor prices, inventory",
            "output": "Optimal price for maximum profit"
        },
        {
            "problem": "Review Sentiment Analysis",
            "input": "Customer review text",
            "output": "Sentiment: Positive / Neutral / Negative"
        }
    ]
}


# -------------------------------
# Step 2: Display Ideas
# -------------------------------
print("=" * 70)
print("              MACHINE LEARNING IDEA GENERATOR")
print("=" * 70)

for domain, ideas in ml_ideas.items():
    print(f"\n{'=' * 12} {domain.upper()} {'=' * 12}")

    for i, idea in enumerate(ideas, start=1):
        print(f"\n  {i}. Problem : {idea['problem']}")
        print(f"     Input   : {idea['input']}")
        print(f"     Output  : {idea['output']}")

print("\n" + "=" * 70)
print("Total Domains:", len(ml_ideas))
print("Total Ideas  :", sum(len(v) for v in ml_ideas.values()))