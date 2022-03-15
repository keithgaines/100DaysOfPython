# Password Generator Project
import random
import string
import os

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Order not randomised:

# picks k number of random letters from string.ascii_letters
# string.ascii_letters includes both capital and lowercase
letters = ''.join(random.choices(string.ascii_letters, k = nr_letters))  

# picks k number of random symbols from string.punctuation
symbols = ''.join(random.choices(string.punctuation, k = nr_symbols))   

# picks k number of random numbers from string.digits
numbers = ''.join(random.choices(string.digits, k = nr_numbers))   

# combines values of letters, symbols, and numbers, into the password variable
password = letters + symbols + numbers

print(f"Your standard generated password is: {password}")
os.system('pause')

#Order of characters randomised:

# converts the password variable to a list and assigns that value to str_var
str_var = list(password)

# randomly shuffles the str_var variable
random.shuffle(str_var)

# joins string_var together as a string and prints the value 
print(''.join(str_var))
os.system('pause')



