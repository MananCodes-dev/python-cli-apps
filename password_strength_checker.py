import re

def check_password_strength(password):
    score = 0

    if len(password) < 8:
        score += 1  # Too short
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score <=2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength

while True:
    pwd = input("Enter a password to check strength")
    result = check_password_strength(pwd)
    print(f"The password strength is: {result}")

    again = input("Do you want to check another password? (yes/no): ").strip().lower()
    if again != 'yes':
        break