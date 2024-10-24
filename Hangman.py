import random
# List of words to guess
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = []

# Create a list to store the blanks for the word
blanks = ["_"] * len(word)

# Hangman art for different stages
hangman_stages = [
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    """,
    """
       ------
       |    |
       |
       |
       |
       |
    """,
    """
       ------
       |
       |
       |
       |
       |
    """
]

# Number of incorrect guesses allowed
max_incorrect_guesses = len(hangman_stages) - 1
incorrect_guesses = 0

# Game loop
while True:
    # Print the current state of the word and hangman art
    print(" ".join(blanks))
    print(hangman_stages[incorrect_guesses])

    # Ask the user for a letter
    letter = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if letter in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    # Add the letter to guessed letters
    guessed_letters.append(letter)

    # Check if the letter is in the word
    if letter in word:
        # Fill in the corresponding blanks
        for i in range(len(word)):
            if word[i] == letter:
                blanks[i] = letter
    else:
        # Increment incorrect guesses
        incorrect_guesses += 1
        print("Incorrect! You got a strike.")

    # Check if the user has won
    if "_" not in blanks:
        print("Congratulations! You won! The word was:", word)
        break

    # Check if the user has lost
    if incorrect_guesses >= max_incorrect_guesses:
        print(hangman_stages[incorrect_guesses])
        print("Game over! The word was:", word)
        break
