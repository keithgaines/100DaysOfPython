from menu import Menu
from money_machine import MoneyMachine

from coffee_maker import CoffeeMaker

# assigns classes to variables
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items  # gets menu items from menu class, and stores them in a variable called "options"
    choice = input(f"What would you like? {options} : ")

    # exits program/turns the machine off if user enters "off"
    if choice == "off":
        is_on = False

    # prints money, and resources remaining, report if user enters "report"
    elif choice == "report":
        print(money_machine.report)
        print(coffee_maker.report)

    # searches for the user input on the menu if the user enters anything else
    else:
        drink = menu.find_drink(choice)
        # if machine has resources available, and payment > drink cost, make the user's drink 
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
