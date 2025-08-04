import random as rd
import string

def generate_password(length): # Function to generate a random password
    if length < 4:
        return "Password length must be at least 4 characters."
    
    characters = string.ascii_letters + string.digits + string.punctuation # Combining letters, digits, and punctuation
    # Randomly selecting characters from the combined string
    password = "".join(rd.sample(characters, length))
    return password

while True:
    print("\nPassword Generator")
    try:
        Length = int(input("Enter the length of the password (minimum 4): "))
        print("Generated Password:", generate_password(Length))
    except ValueError:
        print("Please enter a valid integer for the password length.")

    again = input("Do you want to generate another password? (yes/no): ").strip().lower()
    if again!= 'yes':
        break 