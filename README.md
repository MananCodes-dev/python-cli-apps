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

python number_converter.py
# 🔐 Python Password Strength Checker

This Python CLI tool checks the strength of a password using:
- Length
- Uppercase + lowercase
- Digits
- Special characters

## Output:
- Weak / Medium / Strong

## Run it:
````

python password_strength_checker.py

````

# ✊🖐✌ Rock–Paper–Scissors CLI Game

Python-based CLI version of Rock–Paper–Scissors with score tracking.

## Features:
- User vs computer
- Scoreboard tracking
- Random choices using `random.choice`
- Loops and clean UX

## Run it:
```
python rock_paper_scissors.py
```
# 🎲 Python Dice Rolling Game

A simple command-line dice game using Python's `random` module.

## Features:
- Simulates rolling a 6-sided dice
- Loops for continuous play
- Clean CLI interface

## How to Run:
```
python dice_game.py
```
# ⌨️ Typing Speed Test CLI App

A Python CLI app that measures typing speed and accuracy.

## Features:
- Random sentence selection
- WPM calculation
- Accuracy measurement
- Replayable

## Run it:
```
python typing_speed_test.py
```
# 💰 Python Expense Tracker CLI

A simple Python CLI tool to track expenses in a CSV file.

## Features:
- Add new expense with date, category, note
- View all expenses
- Calculate total spent
- CSV storage for persistence

## Run it:
```bash
python expense_tracker.py
