import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

chosen_number = int(random.choice(range(1, 100)))
successful_guess = False
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while attempts > 0:
        if guess > chosen_number:
            guess = int(input("Too high. Guess again: "))
            attempts -= 1
            input("Guess again: ")
            
        if guess < chosen_number:
            guess = int(input("Too low. Guess again: "))
            attempts -= 1
            
        else:
            print("You guessed it")
            successful_guess == True
    
else: 
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while attempts > 0:
        if guess > chosen_number:
            guess = int(input("Too high. Guess again: "))
            attempts -= 1
            input("Guess again: ")

        if guess < chosen_number:
            guess = int(input("Too low. Guess again: "))
            attempts -= 1
            
        else:
            print("You guessed it")
            successful_guess == True
if attempts == 0:
    print(f"You are out of attempts. The correct number was {chosen_number}. Game over")

