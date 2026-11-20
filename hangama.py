
import random

# Predefined words
words = ["python", "apple", "school", "mobile", "computer"]

# Select a random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== WELCOME TO HANGAMA GAME =====")

while attempts > 0:
    # Display the word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Incorrect guesses left:", attempts)

    # Check winning condition
    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

# Game over
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)
