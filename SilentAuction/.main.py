from art import logo
from replit import clear

# imports a clear() function from replit (the IDE I created this in) to clear the output in the console

print(logo)

bids = {}
continue_bidding = True


# function to find the highest bidder from the bids dictionary
def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        bid_amount = bids[name]  # sets the value of dictionary[key name] to a variable bid_amount
        if int(bid_amount) > int(highest_bid):
            # variable was originally a string type. this casts bid_amount and highest_bid to integers where the > can be used to compare
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while continue_bidding == True:
    name = input("What is your name? ")
    bid_price = input("What is your bid? $")

    bids[name] = bid_price

    new_bidder = input("Is there another bidder? 'yes' or 'no'")
    if new_bidder == "yes":
        continue_bidding = True
        clear()
    else:
        continue_bidding = False
        find_highest_bidder(bids)
