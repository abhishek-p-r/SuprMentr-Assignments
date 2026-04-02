"""
Assignment 25: Prompt Engineer - Weak vs Strong Prompts
Date: 30/03/2026
"""

import textwrap

# ---------------------------------------
# 🧠 Prompt Pairs
# ---------------------------------------
PROMPT_PAIRS = {
    "Resume": {
        "weak": "Write a resume.",
        "strong": (
            "You are an expert career coach and professional resume writer. "
            "Create a one-page resume for a recent Computer Science graduate "
            "(B.Tech, 2024) applying for a junior Machine Learning Engineer role. "
            "Include: summary, skills, internship, projects, education. "
            "Use ATS-friendly format."
        ),
    },

    "Business Idea": {
        "weak": "Give me a business idea.",
        "strong": (
            "You are a startup consultant. Propose ONE business idea for Tier-2 Indian cities "
            "under Rs.10 lakh investment. Include: Problem, Solution, Target Customers, "
            "Revenue Model, Advantage, roadmap."
        ),
    },

    "Study Plan": {
        "weak": "Make a study plan.",
        "strong": (
            "Act as an academic mentor. Create a 4-week NLP study plan with daily topics, "
            "resources, mini-projects, and final capstone."
        ),
    },
}

# ---------------------------------------
# 🤖 Mock AI Function (SIMULATES OUTPUT)
# ---------------------------------------
def call_ai(prompt: str) -> str:
    p = prompt.lower()

    # -------- Resume --------
    if "resume" in p:
        if "expert" in p:
            return (
                "SUMMARY:\nRecent CS graduate skilled in ML.\n\n"
                "SKILLS:\nPython, TensorFlow, SQL\n\n"
                "EXPERIENCE:\nIntern - Image Classification\n\n"
                "PROJECTS:\nML Model, NLP Chatbot\n\n"
                "EDUCATION:\nB.Tech CS (2024)"
            )
        else:
            return "This is a resume with name, education and skills."

    # -------- Business --------
    elif "business" in p:
        if "consultant" in p:
            return (
                "PROBLEM:\nSmall shops lack online reach.\n\n"
                "SOLUTION:\nMobile delivery app.\n\n"
                "CUSTOMERS:\nTier-2 users\n\n"
                "REVENUE:\nCommission model\n\n"
                "ROADMAP:\n3 months launch"
            )
        else:
            return "Start a small shop or online business."

    # -------- Study --------
    elif "study" in p:
        if "mentor" in p:
            return (
                "WEEK 1: Basics\n"
                "WEEK 2: Text processing\n"
                "WEEK 3: ML models\n"
                "WEEK 4: Project\n"
                "CAPSTONE: Build chatbot"
            )
        else:
            return "Study daily and revise."

    return "No response available."


# ---------------------------------------
# 🖨️ Display Helpers
# ---------------------------------------
SEPARATOR = "=" * 60

def print_header():
    print(f"\n{SEPARATOR}")
    print("  ASSIGNMENT 25: PROMPT ENGINEERING DEMO (NO API)")
    print(f"{SEPARATOR}")

def print_category(category):
    print(f"\n{SEPARATOR}")
    print(f"  CATEGORY: {category}")
    print(f"{SEPARATOR}")

def print_block(label, prompt, response):
    short_prompt = textwrap.shorten(prompt, width=80)

    print(f"\n  [{label.upper()} PROMPT]")
    print(f"  Prompt : {short_prompt}")
    print("\n  Response (first 4 lines):")

    lines = [l for l in response.split("\n") if l.strip()]
    for line in lines[:4]:
        print(f"    {line}")

    print("    ...")


# ---------------------------------------
# 🚀 Main Execution
# ---------------------------------------
def main():
    print_header()

    for category, prompts in PROMPT_PAIRS.items():
        print_category(category)

        for label, prompt in prompts.items():
            response = call_ai(prompt)
            print_block(label, prompt, response)


if __name__ == "__main__":
    main()