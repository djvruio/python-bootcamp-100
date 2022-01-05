#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#https://pythontutor.com/
import os
from art import logo

bidders = {}

def ask_bid_info():
    name = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))
    bidders[name] = bid_price

def define_winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bid in bidding_record:
        bid_amount = bidding_record[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    print(f'The winner is: {winner} with a bid of: ${highest_bid}')

print(logo)
print("Welcome to the secret auction program.")

exists_other_bidders = True # bidding_finished is a better varable name
ask_bid_info()

while exists_other_bidders:
    user_response = input("Are there other bidders? Type 'yes' or 'no': ") # should_continue is a better varable name
    if user_response == 'yes':
        os.system('cls')
        ask_bid_info()
    else:
        exists_other_bidders = False
        define_winner(bidding_record=bidders)

#print("--------------------\n",bidders)