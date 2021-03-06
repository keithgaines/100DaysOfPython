# Password Generator Project
import os
import random

# creates the lists "letters," "numbers," and "symbols"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Standard Pattern (order not randomized)
password = ""

# for character in range from 1 - user input number of how many characters they want+1
# add randomly selected character from list to the end of the password string
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(f"Your standard generated password is: {password})
os.system('pause')

# Order randomized

# creates a blank list called password_list
password_list = []

# for character in range from 1 - user input number of how many characters they want+1
# add randomly selected character from list to the end of the password list
for char in range(1, nr_letters + 1):
    password_list += (random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# shuffles the password_list list
random.shuffle(password_list)

# creates a blank string called password
password = ""

# adds shuffled items from password_list to the password string
for char in password_list:
    password += char

# prints the completed password string
print(f"Your password is: {password}")
os.system('pause')
