import random

options = ["rock", "paper", "scissors"]
user_choice = 0
computer_score = 0
rounds = 0

print("Welcome to Rock, Paper, Scissors!")

while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    if user not in options:
        print("Invalid choice. Please try again.")
        continue
    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win!")
        user_choice += 1
    else:
        print("Computer wins!")
        computer_score += 1

    rounds += 1
    print(f"Score + You: {user_choice}, Computer: {computer_score}, Rounds: {rounds}")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != 'yes':
        break

print("Thanks for playing!")