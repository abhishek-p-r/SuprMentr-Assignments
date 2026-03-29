# ==========================================
# Assignment 1: Password Authentication System
# Date: 07/02/2026
# ==========================================

import hashlib
import getpass
import json
import os
import re
from datetime import datetime

CREDENTIALS_FILE = "users.json"
MAX_ATTEMPTS = 3


# -------------------------------
# File Handling
# -------------------------------

def load_users() -> dict:
    """Load users from JSON file"""
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    return {}


def save_users(users: dict):
    """Save users to JSON file"""
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(users, file, indent=4)


# -------------------------------
# Security Functions
# -------------------------------

def hash_password(password: str) -> str:
    """Hash password with salt"""
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}:{hashed}"


def verify_password(stored: str, provided: str) -> bool:
    """Verify entered password"""
    salt, hashed = stored.split(":")
    check_hash = hashlib.sha256((provided + salt).encode()).hexdigest()
    return hashed == check_hash


def validate_password(password: str) -> tuple:
    """Check password strength"""
    if len(password) < 8:
        return False, "Minimum 8 characters required"
    if not re.search(r"[A-Z]", password):
        return False, "At least one uppercase letter required"
    if not re.search(r"[a-z]", password):
        return False, "At least one lowercase letter required"
    if not re.search(r"\d", password):
        return False, "At least one digit required"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "At least one special character required"

    return True, "Strong password"


# -------------------------------
# Core Features
# -------------------------------

def register_user():
    """Register a new user"""
    users = load_users()

    print("\n--- Register ---")
    username = input("Enter username: ").strip()

    if not username:
        print("Username cannot be empty.")
        return

    if username in users:
        print("Username already exists.")
        return

    while True:
        password = getpass.getpass("Enter password: ")
        valid, message = validate_password(password)

        if not valid:
            print(f"Weak password: {message}")
            continue

        confirm = getpass.getpass("Confirm password: ")
        if password != confirm:
            print("Passwords do not match.")
            continue

        break

    users[username] = {
        "password": hash_password(password),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "failed_attempts": 0,
        "locked": False
    }

    save_users(users)
    print(f"User '{username}' registered successfully!")


def login_user() -> bool:
    """Login user"""
    users = load_users()

    print("\n--- Login ---")
    username = input("Enter username: ").strip()

    if username not in users:
        print("User not found.")
        return False

    if users[username]["locked"]:
        print("Account is locked.")
        return False

    password = getpass.getpass("Enter password: ")

    if verify_password(users[username]["password"], password):
        users[username]["failed_attempts"] = 0
        save_users(users)
        print(f"\nWelcome, {username}! Login successful.")
        return True

    else:
        users[username]["failed_attempts"] += 1
        remaining = MAX_ATTEMPTS - users[username]["failed_attempts"]

        if remaining <= 0:
            users[username]["locked"] = True
            print("Too many attempts. Account locked.")
        else:
            print(f"Incorrect password. {remaining} attempts left.")

        save_users(users)
        return False


def reset_user_password():
    """Reset password"""
    users = load_users()

    print("\n--- Reset Password ---")
    username = input("Enter username: ").strip()

    if username not in users:
        print("User not found.")
        return

    while True:
        password = getpass.getpass("Enter new password: ")
        valid, message = validate_password(password)

        if not valid:
            print(f"Weak password: {message}")
            continue

        confirm = getpass.getpass("Confirm password: ")
        if password != confirm:
            print("Passwords do not match.")
            continue

        break

    users[username]["password"] = hash_password(password)
    users[username]["failed_attempts"] = 0
    users[username]["locked"] = False

    save_users(users)
    print("Password reset successfully!")


# -------------------------------
# Main Menu
# -------------------------------

def main():
    print("=== Password Authentication System ===")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Reset Password")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            reset_user_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Entry Point
if __name__ == "__main__":
    main()