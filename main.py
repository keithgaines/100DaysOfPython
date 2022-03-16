from game_data import data
import random
from art import logo, vs
import os

def get_random_account():
  """selects random account from data in game_data"""
  return random.choice(data)

def format_data(account):
  """assigns name/description/country from data to variables of the same name, and prints the information"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a" # returns True because double equal sign checks if variable is equal to value. if A has more followers than b, and the user guessed a, then  guess (a) is equal to "a" and the statement returns true
  else:
    return guess == "b" # if b_followers > a_followers and guess == b, then the statement returns true because guess is equal to "b". otherwise, the statement returns false


def game():
  print(logo)
  score = 0
  game_over = False
  account_a = get_random_account()
  account_b = get_random_account()

  # replaces account_a with account_b 
  # gets a new random account as account_b
  while not game_over:
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # assigns follower count value from dictionary to follower_count variable for accounts a and b
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # checks answer and assigns the returned True or False value to the variable is_correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clears screen
    os.system('cls') 

    print(logo)
    if is_correct: # if is_correct is true
      score += 1
      print(f"Correct! Current score: {score}.")
    else:
      game_over = True
      print(f"Sorry, that's wrong. Final score: {score}")
      input("Press any key to end program...")

game()
