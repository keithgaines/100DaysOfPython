import os
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

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

choices = [rock, paper, scissors]

if player_choice == "0":
    player_choice = choices[0]
elif player_choice == "1":
    player_choice = choices[1]
else:
    player_choice = choices[2]

computer_choice = random.choice(choices)

print(f"you chose:", player_choice)
print(f"computer chose:", computer_choice)

if player_choice == computer_choice:
    print("It's a draw!")
    os.system('pause')
elif player_choice == [0] and computer_choice == [1]:
    print("You lose")
    os.system('pause')
elif player_choice == [0] and computer_choice == [2]:
    print("You win")
    os.system('pause')
elif player_choice == [1] and computer_choice == [0]:
    print("You win")
    os.system('pause')
elif player_choice == [1] and computer_choice == [2]:
    print("You lose")
    os.system('pause')
elif player_choice == [2] and computer_choice == [0]:
    print("You lose")
    os.system('pause')
else:
    print("You win")
    os.system('pause')
