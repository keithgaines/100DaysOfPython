from game_data import data
import random
from art import logo, vs

# selects random account from data in game_data
def get_random_account():
  return random.choice(data)

# assigns name/description/country from data to variables of the same name
# returns the information in a printable form
def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


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
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print(logo)
    if is_correct:
      score += 1
      print(f"Correct! Current score: {score}.")
    else:
      game_over = True
      print(f"Sorry, that's wrong. Final score: {score}")
      input("Press any key to end program...")

game()

