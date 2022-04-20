import os
from art import logo
import math

bids = {}

def blind_auction():
    os.system('clear')
    print(logo)
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    other_bids = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    add_bids(name, bid)
    
    if other_bids == "yes":
        return  blind_auction()
    elif other_bids == "no":
        return get_winner()

def add_bids(name, bid):
    bids[name] = bid

def get_winner():
    winner = ""
    max = 0
    for key in bids:
        if bids[key] > max:
            winner = key
            max = bids[key]
    print(f"The winner is {winner} with a bid of ${math.ceil(max)}")


blind_auction()





