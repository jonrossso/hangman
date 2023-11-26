import milestone_2

def check_guess(guess):
    while True:
        if guess in milestone_2.randomly_selected_word_in_fruit_word_list:
            print(f"{guess} exists within the word!")
            break
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            print(f"Good guess! {guess} is in the word.")
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()


