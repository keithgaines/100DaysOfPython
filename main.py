############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

game_over = False

# restarts the game and prints the logo
def start_game(): 
    print(logo)

# returns a randomly selected item from the cards list
def deal_card():
    card = random.choice(cards)
    return card

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

# loops through twice and adds the returned value of deal_card() to the end of the user_cards and computer_cards list
for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2: # checks for Blackjack with an ace and a face card (2 cards with a combined value of 21)
    return 0 # returns 0 for Blackjack if the if statement is true
  # checks for an ace (value 11) and if the value of cards is over 21, replaces the ace value 11 with an ace value of 1
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
        if user_score > 21 and computer_score > 21:
            return "Bust. You lose"
        if user_score == computer_score:
            return "It's a draw"
        elif computer_score == 0:
            return "You lose. Opponent has Blackjack"
        elif user_score == 0:
            return "Blackjack. You win!"
        elif user_score > 21:
            return "Bust. You lose."
        elif computer_score > 21:
            return "Opponent bust. You win"
        elif user_score > computer_score:
            return "You win"
        else:
            return "You lose"

while game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    draw_again = input("Do you want another card? Type 'y' for yes, or 'n' for no.")
    if draw_again == "y":
        user_cards.append(deal_card)
    else: 
        game_over = True
    
    # computer will continue to draw cards as long as the value of computer_cards is below 17
    while computer_score < 17:
        computer_cards.append(deal_card)

    # compares user score and computer score to display results of the game
    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  start_game()



