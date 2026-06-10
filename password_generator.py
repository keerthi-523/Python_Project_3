# ==========================================
# Project 3: Random Password Generator
# Developed for DecodeLabs Internship
# ==========================================

import random
import string


def generate_password(length):
    """
    Generates a secure random password
    using uppercase, lowercase letters,
    digits and special characters.
    """

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+"

    all_characters = lowercase + uppercase + digits + special_chars

    password = []

    # Ensure password contains at least one character from each category
    password.append(random.choice(lowercase))
    password.append(random.choice(uppercase))
    password.append(random.choice(digits))
    password.append(random.choice(special_chars))

    # Fill remaining length
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle password for randomness
    random.shuffle(password)

    return "".join(password)


def password_strength(length):
    """
    Returns password strength based on length.
    """
    if length < 8:
        return "Weak"
    elif length < 12:
        return "Medium"
    else:
        return "Strong"


def main():
    print("=" * 50)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 50)

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        print("\nPassword Strength:")
        print(password_strength(length))

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()