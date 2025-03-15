import random
import string


def generate_password(nr_letters, nr_symbols, nr_numbers, randomize=True):
    """
    Generate a password with the specified number of letters, symbols, and numbers.
    If randomize is True, the characters will be in random order.
    """
    # Use string module for character sets
    letters = list(string.ascii_letters)  # both upper and lowercase
    numbers = list(string.digits)  # 0-9
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '?', '@', '^']

    # Create password components
    password_list = []

    # Add requested letters
    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    # Add requested symbols
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    # Add requested numbers
    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    # Randomize if requested
    if randomize:
        random.shuffle(password_list)

    # Convert list to string
    password = ''.join(password_list)
    return password


def check_password_strength(password):
    """
    Evaluate the strength of a password and provide feedback.
    Returns a dictionary with strength rating and suggestions
    """
    score = 0
    feedback = []

    # Check length
    if len(password) >= 15:  # Preferred length for high-security
        score += 3
        feedback.append("Excellent password length")
    elif len(password) >= 12:
        score += 2
        feedback.append("Good password length")
    elif len(password) >= 8:  # Minimum acceptable length
        score += 1
        feedback.append("Meets minimum password length. \nConsider a longer length and a password manager "
                        "to increase your security and decrease your stress.")
    else:
        feedback.append("Password must have a minimum of 8 characters")

    # Character variety checks (informational, not required by NIST)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!#$%&()*+?@^' for c in password)

    # Count how many character types are used
    character_types_used = sum([has_lower, has_upper, has_digit, has_special])

    # Provide feedback based on variety
    if character_types_used <= 2:
        feedback.append("Consider using a mix of character types and a password manager "
                        "to increase your security and decrease your stress.")
    # Determine strength level
    if score >= 3:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Minimal"

    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }


def main():
    print(r'''
     8 8          ,o.                                        ,o.          8 8
    d8o8azzzzzzzzd   b                                      d   bzzzzzzzza8o8b
                  `o'                                        `o'  
    ''')
    print("Welcome to the Jenn-erator - Password Generator!")
    print("_____________________________________________")

    try:
        # Get user input
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))

        # Generate password
        password = generate_password(nr_letters, nr_symbols, nr_numbers)

        # Check Strength
        strength_info = check_password_strength(password)

        # Display results
        print("\n-------------------------------------")
        print(f"Your password is: {password}")
        print(f"Length: {len(password)} characters")
        print(f"Strength: {strength_info['strength']} {strength_info['score']}/3")

        # Display feedback if available
        if strength_info['feedback']:
            print("\nFeedback:")
            for tip in strength_info['feedback']:
                print(f"- {tip}")

    except ValueError:
        print("Please enter valid numbers for the password criteria.")


if __name__ == "__main__":
    main()
