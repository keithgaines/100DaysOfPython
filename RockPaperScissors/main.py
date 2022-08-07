import random

rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
play_game = True
def game():
    while play_game == True:
        player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

        choices = [rock, paper, scissors]

        if player_choice == "0":
            player_choice = choices[0]
        elif player_choice == "1":
            player_choice = choices[1]
        elif player_choice == "2":
            player_choice = choices[2]

        computer_choice = random.choice(choices)

        if computer_choice == choices[0]:
            computer_choice == rock
        elif computer_choice == choices[1]:
            computer_choice == paper
        elif computer_choice == choices[2]:
            computer_choice == scissors

        print(f"you chose:", player_choice)
        print(f"computer chose:", computer_choice)

        if player_choice == computer_choice:
            print("It's a draw!")
            
        elif player_choice == rock and computer_choice == paper:
            print("You lose")
            
        elif player_choice == rock and computer_choice == scissors:
            print("You win")
            
        elif player_choice == paper and computer_choice == rock:
            print("You win")
            
        elif player_choice == paper and computer_choice == scissors:
            print("You lose")
            
        elif player_choice == scissors and computer_choice == rock:
            print("You lose")

        elif player_choice == scissors and computer_choice == paper:
            print("You win")

        play_again = input("Do you want to play again? y or n: ")
        
        if play_again == 'y':
            play_game == True
        else:
            break
game()

        
