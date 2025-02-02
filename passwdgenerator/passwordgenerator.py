import random
import string

def generate_password(length=12):
    """Generate a random password."""
    if length < 6:
        print("Password length should be at least 6 characters.")
        return None

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password has at least one character from each set
    all_characters = lowercase + uppercase + digits + special_characters
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# User input for password length
try:
    length = int(input("Enter the desired password length (minimum 6): "))
    password = generate_password(length)
    if password:
        print(f"Generated password: {password}")
except ValueError:
    print("Please enter a valid number.")
