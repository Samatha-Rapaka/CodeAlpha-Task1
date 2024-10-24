# CodeAlpha-Task1
<h1>Hangman Game in Python</h1>
In this tutorial, we will create a simple hangman game in Python. The game will randomly select a word from a pre-defined list of words and the player will have to guess the word by guessing individual letters. The game will keep track of the number of lives remaining and will display ASCII art corresponding to the number of lives remaining. The game will end when the word has been fully guessed or when the player runs out of lives.
<h2>Prerequisites</h2>
- Basic knowledge of Python programming<br>
- Familiarity with loops and conditional statements
<h2>Explanation of the Code</h2>
<h3>1.Word Selection:</h3> A random word is chosen from a predefined list.
<h3>2.Game State:</h3> The game maintains the current state of guessed letters and blanks.
<h3>3.Hangman Art:</h3> An array of strings represents the hangman at various stages of the game. Each incorrect guess corresponds to a different stage of the hangman drawing.
<h3>4.Game Loop:</h3> The loop continues until the user either guesses the word or reaches the maximum number of incorrect guesses.
<h3>5.User Input:</h3> The user is prompted to guess a letter, and the game checks if the letter has already been guessed.
<h3>6.Win/Loss Conditions:</h3> The game checks if the user has guessed the word or has reached the maximum incorrect guesses.
