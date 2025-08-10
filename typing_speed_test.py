import time
import random

sentences = [
    "Python is a amazing programming language",
    "Artificial Intelligence is changing the world",
    "Machine Learning powers many modern applications",
    "Game devlopment is both art and Logic",
    "Data Science is a field of study that uses scientific methods",
]

print("Welcome to the Typing Speed Test!")

while True:
    sentence = random.choice(sentences)
    print(f"Type the following sentence:\n{sentence}")

    input("Press Enter when you are ready to start...")
    start_time = time.time()
    typed_sentence = input("Start typing: ")
    end_time = time.time()

    time_taken = end_time - start_time
    words_typed = len(typed_sentence.split())
    wpm = words_typed / (time_taken / 60)

    #Accuracy calculation
    correct_words = sum(1 for t, s in zip(typed_sentence.split(), sentence.split()) if t == s)
    accuracy = (correct_words / len(sentence.split())) * 100

    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

    again = input("Do you want to try another sentence? (yes/no): ").lower()
    if again != 'yes':
        break
print("Thanks for playing the Typing Speed Test!")
