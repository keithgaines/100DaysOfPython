import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# chooses a random number from a range of 1 - 100 cast as an integer
chosen_number = int(random.choice(range(1, 100)))

# if statement that assigns number of attempts based on difficulty
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

# assigns user guess to variable 'guess' and casts it as an int from a string
guess = int(input("Make a guess: "))

while attempts > 0:
    if guess > chosen_number:
        guess = int(input("Too high. Guess again: "))
        attempts -= 1

    if guess < chosen_number:
        guess = int(input("Too low. Guess again: "))
        attempts -= 1

    if guess == chosen_number:
        print("You guessed it")
        attempts = 0

if attempts == 0:
    print(f"The correct number was {chosen_number}. Game over")
    input("Press enter to end the program...")
