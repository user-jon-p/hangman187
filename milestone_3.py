def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''

        while True:
            letter = input("Guess a letter: ").strip().lower()

            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single alphabetical character.")
            elif letter in self.list_letters:
                print(f"{letter} was already tried.")
            else:
                self.check_letter(letter)
                break
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        pass

def check_letter(self, letter) -> None:
    
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        
        letter = letter.lower()

        if letter in self.list_letters:
            print(f"{letter} was already tried.")
            return

        self.list_letters.append(letter)

        if letter in self.word:
            print(f"Good job! '{letter}' is in the word.")
            for i, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[i] = letter
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Wrong guess! '{letter}' is not in the word. Lives left: {self.num_lives}")
        
        print(" ".join(self.word_guessed))

        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        pass


def check_guess(self, guess):
        """Checks if the guess is in the word."""
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')