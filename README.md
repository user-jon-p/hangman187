# Hangman Game

## Description
A simple Hangman game where the player guesses letters to reveal a mystery word. The game provides feedback on correct and incorrect guesses and tracks the number of lives remaining.

## How to Play
- The game randomly selects a word from a predefined list.
- The player guesses letters one at a time.
- If the guessed letter is in the word, it is revealed in its correct position.
- If the guessed letter is incorrect, the player loses a life.
- The game continues until the player either guesses the word correctly or runs out of lives.

## Features
- Random word selection from a predefined list.
- Input validation to ensure only single alphabetical characters are entered.
- Tracks guessed letters to prevent duplicate guesses.
- Provides feedback on correct and incorrect guesses.
- Displays the current state of the word and the number of remaining lives.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd hangman187
   ```
3. Run the script:
   ```sh
   python hangman.py
   ```

## File Structure
- `hangman.py`: Main script containing the Hangman game logic.
- `README.md`: Documentation about the project.

## Code Explanation
### `Hangman` Class
- **`__init__`**: Initializes game attributes including the word, guessed letters, remaining lives, and list of previous guesses.
- **`check_guess(guess)`**: Checks if the guessed letter is in the word and updates the game state accordingly.
- **`ask_for_input()`**: Handles user input validation and calls `check_guess()`.

### `play_game(word_list)` Function
- Creates an instance of `Hangman` and manages the game loop.
- Ends the game when the player wins or runs out of lives.

## Example Output
```
The mystery word has 6 characters.
_ _ _ _ _ _
Guess a letter: a
Good guess! 'a' is in the word.
_ a _ _ _ a
Guess a letter: z
Sorry, 'z' is not in the word.
You have 4 lives left.
```

## License
This project is licensed under the MIT License.
