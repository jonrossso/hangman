import random
import milestone_2

class Hangman:
    # Initialising this game with a list of words and a set number of lives
    # Initialising this game with a list of words and a set number of lives
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list  # Listing the possible words to guess
        self.num_lives = num_lives  # Number of allowed incorrect guesses
        self.word = random.choice(self.word_list)  # Randomly selecting a word from the list
        self.word_guessed = ["_" for _ in self.word]  # Creating a list of underscores representing the word to guess
        self.num_letters = len(set(self.word))  # Counting unique letters in the word to be guessed
        self.word = random.choice(self.word_list)  # Randomly selecting a word from the list
        self.word_guessed = ["_" for _ in self.word]  # Creating a list of underscores representing the word to guess
        self.num_letters = len(set(self.word))  # Counting unique letters in the word to be guessed
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
            # Decreasing the count of unique letters left if the guessed letterr is correct and new
            # Decreasing the count of unique letters left if the guessed letterr is correct and new
            if guess not in self.list_of_guesses:
                self.num_letters -= 1
        else:
            # Decreasing the number of lives and informing the playyer if if the guess is wrong
            # Decreasing the number of lives and informing the playyer if if the guess is wrong
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
                    
    # Prompting the player to guess a letter and handle the guess
    # Prompting the player to guess a letter and handle the guess
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()  # Getting input from the user and lowering the case
            # Validating the input
            # Validating the input
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Checking guesses
                # Checking guesses
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break

        

        

if __name__ == "__main__":
    # Starting game with list of fruits from milestone_2
    # Starting game with list of fruits from milestone_2
    game = Hangman(milestone_2.fruit_word_list)
    # Beginning the game by asking for the first guess
    # Beginning the game by asking for the first guess
    game.ask_for_input()
