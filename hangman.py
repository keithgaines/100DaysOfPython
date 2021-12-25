import random
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# imports the logo from the hangman_art file and prints it at the beginning
from hangman_art import logo
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # if the user guesses a letter they've already guessed, prints a statement letting them know
    if guess in display:
        print(f"You've already guessed {guess}")

    # checks guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        # if the letter is not in the chosen_word, prints out the letter and let them know it's not in the word
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # joins all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    # checks if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # imports stages ASCII art from hangman_art file and prints them based on how many lives are left
    from hangman_art import stages
    print(stages[lives])
