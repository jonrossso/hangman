import random

fruit_word_list = ["grapes", "tangerines", "oranges", "apples", "watermelons"]

class Hangman:
    """
    This class represents the entire  game and is responsible for the game state of Hangman,
    including tracking the number of lives, the word to guess, and the progress on the current word.

    Attributes:
        word_list (list): The list of potential words to guess.
        num_lives (int): The number of incorrect guesses allowed before the game is lost.
        word (str): The word that needs to be guessed.
        word_guessed (list): The current state of the word being guessed, with unguessed letters as underscores.
        num_letters (int): The number of unique letters in the word that need to be guessed.
        list_of_guesses (list): The letters that have been guessed so far.
    """

    def __init__(self, word_list, num_lives = 5):
        """
        Initialises a new game with a given list of words and a set number of lives.
        """
        self.word_list = word_list  # Listing the possible words to guess
        self.num_lives = num_lives  # Number of allowed incorrect guesses
        self.word = random.choice(self.word_list)  # Randomly selecting a word from the list
        self.word_guessed = ["_" for _ in self.word]  # Creating a list of underscores representing the word to guess
        self.num_letters = len(set(self.word))  # Counting unique letters in the word to be guessed
        self.list_of_guesses = []  # Keeping track of the letters guessed so far

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state accordingly.
        """
        guess = guess.lower()  # Converting the guess to lowercase for consistency
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            # Revealing the guessed letter in the word
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            # Decreasing the count of unique letters left if the guessed letter is correct and new
            if guess not in self.list_of_guesses:
                self.num_letters -= 1
        else:
            # Decreasing the number of lives and informing the playyer if if the guess is wrong
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
                    

    def ask_for_input(self):
        """
        Prompts the player to guess a letter and processes the input.
        """
        while True:
            guess = input("Guess a letter: ").lower()  # Getting input from the user and lowering the case
            # Validating the input
            if not (guess.isalpha() and len(guess) == 1):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                # Checking guesses
                self.check_guess(guess)      
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """
    Initialises the game, prompts the user for input, and checks the game state to determine
    if the game has been won or lost. Prints appropriate messages upon game conclusion.
    """
    game = Hangman(word_list, num_lives = 5)
    while True:
        if  game.num_lives == 0:
            print("You lost!")
            print(f"Randomly selected word: {game.word}")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")
            print(f"Randomly selected word: {game.word}")
            break

if __name__ == "__main__":
    # Starting the game
    play_game(fruit_word_list)