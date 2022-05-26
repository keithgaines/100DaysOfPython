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

import os
import random

from art import logo


# returns a randomly selected item from the cards list
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# compares user and computer score then displays results of the game
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21 or user_score == computer_score:
        return "It's a draw"
    if computer_score == 0:
        return "You lose. Opponent has Blackjack"
    if user_score == 0:
        return "Blackjack. You win!"
    if user_score > 21:
        return "Bust. You lose."
    if computer_score > 21:
        return "Opponent bust. You win"
    if user_score > computer_score:
        return "You win"
    return "You lose"


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # if ace value of 11 is detected, and score is currently over 21, this removes the 11 value and replaces it with a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    print(logo)
    user_cards = []  # creates empty list called user cards
    computer_cards = []  # creates empty list called computer cards
    game_over = False

    # loops through twice and adds the returned value of deal_card() to the end of the user_cards and computer_cards list
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_over == False:
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        # sets game over if user or computer has blackjack, or if the computer busts
        if (user_score == 0) or (computer_score == 0) or (user_score > 21):
            game_over = True
        else:
            draw_again = input("Do you want another card? Type 'y' for yes, or 'n' for no. ")
            if draw_again == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
                print(compare(user_score, computer_score))
                os.system('pause')

    # computer will continue to draw cards as long as the value of computer_cards is below 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card)
        computer_score = calculate_score(computer_cards)


if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
