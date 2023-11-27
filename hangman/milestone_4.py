import random
import milestone_2

class Hangman:
    # Initialising this gamee with a list of words and a set number of lives
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list  # Listing the possible words to guess
        self.num_lives = num_lives  # Number of allowed incorrect guesses
        self.word = random.choice(self.word_list)  # Randomly select a word from the list
        self.word_guessed = ["_" for _ in self.word]  # Create a list of underscores representing the word to guess
        self.num_letters = len(set(self.word))  # Count of unique letters in the word to be guessed
        self.list_of_guesses = []  # Keeping track of the letters guessed so far

    # Method to check a player's guess
    def check_guess(self, guess):
        guess = guess.lower()  # Converting the guess to lowercase for consistency
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            # Revealing the guessed letter in the word
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # If the guessed letter is correct and new, decrease the count of unique letters left
            if guess not in self.list_of_guesses:
                self.num_letters -= 1
        else:
            # If the guess is wrong, decrease the number of lives and inform the player
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
                    
    # Prompt the player to guess a letter and handle the guess
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()  # Getting input from the user and lowering the case
            # Validate the input
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # If valid and new, check the guess and exit 
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

# Entry point
if __name__ == "__main__":
    # Start a game with a list of fruits from milestone_2
    game = Hangman(milestone_2.fruit_word_list)
    # Begin the game by asking for the first guess
    game.ask_for_input()