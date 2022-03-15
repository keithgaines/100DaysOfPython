import os

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

which_way = input("You're at a fork in the road. Which way do you go? Left or right?\n")
which_way = which_way.lower()

if which_way == "left":
    swim = input("You've come to a river. Do you swim across or wait for a boat? Enter 'swim' or 'wait.' \n")
    swim = swim.lower()
    
    if swim == "wait":
        which_door = input("You see three doors. Pick one. Red, yellow, or blue? \n")
        which_door = which_door.lower()
        
        if which_door == "yellow":
            print("Congratulations. You found the treasure.")
            os.system('pause')
        elif which_door == "red":
            print("Upon turning the knob, the door erupts into flames. You are toast.")
            os.system('pause')
        else:
            print("Opening the door triggers a lone record player in the room. Eiffel 65's hit song 'I'm Blue' begins to play. It immediately gets stuck in your head forever. Madness is imminent. Game over.")
            os.system('pause')
    else: 
        print("The river is full of electric eels that attack as soon as you step foot in the water. Game over.")
        os.system('pause')
else: 
    print("You continue walking a lonely road. Realizing you've gone the wrong way, you turn around to find nothing but straight road. There is no going back. Game over.")
    os.system('pause')
