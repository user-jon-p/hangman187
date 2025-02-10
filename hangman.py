import random

class Hangman:
    """
    A Hangman game where the player guesses letters in a mystery word.
    """
    def __init__(self, word_list, num_lives=5):
        """Initializes the Hangman game attributes."""
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        print(f"The mystery word has {len(self.word)} characters.")
        print(" ".join(self.word_guessed))

    def check_guess(self, guess):
        """Checks if the guessed letter is in the word."""
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
        print(" ".join(self.word_guessed))

    def ask_for_input(self):
        """Asks the user for a letter and validates the input."""
        while True:
            guess = input("Guess a letter: ").strip().lower()
            if not (len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

def play_game(word_list):
    """Runs the Hangman game."""
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
