# 🗒 Python Notes App

Simple CLI note-taking tool using file handling in Python.  
Notes are stored in `notes.txt` and can be viewed or deleted later.

## Features:
- Add text notes
- View saved notes
- Delete all notes

## How to Run
python notes_app.py

import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short!"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(characters, length))
    return password

while True:
    print("\n🔐 Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        print("Your password:", generate_password(length))
    except ValueError:
        print("Please enter a number.")

    again = input("Generate another? (yes/no): ").lower()
    if again != 'yes':
        break
# 🧮 Python Mini Calculator

Command-line calculator built in Python.  
Handles basic arithmetic operations and invalid inputs using `try...except`.

## Features:
- Addition, subtraction, multiplication, division
- Input validation
- Division by zero check
- Simple CLI interaction


# 🔢 Python Number System Converter

CLI tool to convert between Binary, Decimal, and Hexadecimal numbers.

## Features:
- Binary ↔ Decimal
- Decimal ↔ Binary
- Decimal ↔ Hex
- Hex ↔ Decimal
- Input validation included

## How to Run:
```bash
python number_converter.py

