# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


# Hangman Game in Python

## Table of Contents
- [Project Overview](#project-overview)
- [What It Does](#what-it-does)
- [Aim](#aim)
- [What I Learned](#what-i-learned)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Code Explanation](#code-explanation)
  - [Word List and Random Selection](#word-list-and-random-selection)
  - [User Input and Validation](#user-input-and-validation)
- [License](#license)

---

## Project Overview
This project implements the classic game of Hangman in Python. The game randomly selects a word from a predefined list, and the player must guess the letters in the word within a limited number of attempts.

## What It Does
- The program starts by randomly choosing a word from a predefined list of fruits.
- It prompts the user to guess a letter.
- It validates the user's input to ensure it's a single alphabetical character.
- It provides feedback to the user on whether their guess is correct or not.
- (Future improvements: Implementing incorrect guess tracking and displaying the Hangman figure.)
- The game continues until the player either correctly guesses the word or runs out of attempts.

## Aim
The primary aim of this project is to:
- Practice fundamental Python programming concepts, including:
  - Working with lists and strings
  - Using the `random` module for word selection
  - Handling user input with the `input()` function
  - Implementing conditional logic (`if-else` statements) for input validation
- Develop a simple, interactive, and playable game.
- Gain experience in structuring a Python project and documenting it with a README file.

## What I Learned
- How to use the `random.choice()` function to select a random word.
- Best practices for handling user input and validation in Python.
- The importance of clear and concise project documentation.

## Installation
1. Ensure you have Python installed (Python 3.x recommended).
2. Clone this repository or download the script.
   ```sh
   git clone https://github.com/yourusername/hangman-game.git
   ```
3. Navigate to the project folder.
   ```sh
   cd hangman-game
   ```
4. Run the script.
   ```sh
   python hangman.py
   ```

## Usage
- Run the script in a terminal or command prompt.
- Follow the on-screen instructions to guess letters.
- Continue guessing until you either:
  - Successfully guess the word.
  - Run out of attempts.

## File Structure
```
/hangman-game
│-- hangman.py  # Main script file
│-- words.txt   # Contains the list of words (if applicable)
│-- README.md   # Project documentation
```

## Code Explanation
### Word List and Random Selection
- The program uses a predefined list of words.
- It randomly selects one word using:
  ```python
  import random
  word = random.choice(word_list)
  ```

### User Input and Validation
- The game ensures user input is valid by checking:
  ```python
  if len(guess) == 1 and guess.isalpha():
      # Process guess
  else:
      print("Invalid input. Please enter a single letter.")
  ```

## License
This project is licensed under the MIT License.

---

> **Note:** This README will be updated as new features are implemented.

