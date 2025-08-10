import random
import itertools

roll_count = 0
for _ in itertools.count():
    roll = input("Roll the dice? (yes/no): ").lower()
    if roll == 'yes':
        roll_count += 1
        dice_value = random.randint(1, 6)
        print(f"You rolled a {dice_value}")
    elif roll == 'no':
        times_str = "time" if roll_count == 1 else "times"
        print(f"\nYou rolled the dice {roll_count} {times_str}.")
        print("Thanks for playing!")
        break
    else:
        print("Please type yes or no.")
# This is a simple dice game where the user can roll a dice or exit the game.